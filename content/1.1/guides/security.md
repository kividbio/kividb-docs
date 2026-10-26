---
title: "Security"
description: "Protect a KiviDB server: protected mode, passwords, users and ACL rules, TLS, the cluster bus, and the commands to keep from clients."
version: "1.1"
weight: 50
---

A KiviDB server holds whatever its clients put in it, and does whatever any client that can connect and log in asks: read every key, delete them all, change its settings. Protect it by who can reach it, who can log in, and what each one may do.

## Who can reach it

Keep the server on a private network, with a firewall in front of its port (6380) and, in a cluster, its bus port (6380 + 10000). A server reachable from the internet will be found.

### Protected mode

A server started without a password, and without [`bind`](../reference/configuration.md#bind), accepts clients from its own machine only; others are refused, with a reply that says why:

```
-DENIED KiviDB is running in protected mode because protected mode is enabled and no password is set for the default user. ...
```

That is [protected mode](../reference/configuration.md#protected-mode). It stops applying as soon as the `default` user has a password, `bind` is given (any address, even `0.0.0.0`), or `protected-mode no` is set. It is checked when a client connects. In Redis 7 and later, `bind` alone does not turn it off.

The Docker image starts the server with `--protected-mode no`, since a container's clients are never on its loopback address; arguments given to `docker run` replace that. Set a password.

## Who can log in

### A password

```
kividb --requirepass "a long random password"
```

Clients then log in before anything else:

```
> PING
(error) NOAUTH Authentication required.
> AUTH "a long random password"
OK
```

Before logging in, a client may send only `AUTH`, `HELLO` with `AUTH`, `QUIT` and `RESET`, of at most 10 arguments of 16 KB each. [`ACL GENPASS`](../commands/acl-genpass.md) makes a good password.

There is no delay after a wrong password, as in Redis: with a password that is short enough to guess, a client that can connect can try many a second. Use a long, random one. Passwords are kept as their SHA-256.

### Users

Beyond the `default` user, [`ACL SETUSER`](../commands/acl-setuser.md) makes users, each with its own passwords and what it may do. A new user starts with no rights:

```
> ACL SETUSER app on >app-password ~app:* +@read +@write -@dangerous
OK
> ACL SETUSER reporting on >report-password %R~* +@read
OK
```

A client logs in as one with `AUTH username password`. What it is refused gets `NOPERM`:

```
> AUTH app app-password
OK
> SET app:1 x
OK
> SET other x
(error) NOPERM User app has no permissions to access the 'other' key
> FLUSHALL
(error) NOPERM User app has no permissions to run the 'flushall' command
```

| Rule | Means |
|---|---|
| `on`, `off` | The user can log in, or not. |
| `>password`, `<password`, `#sha256`, `nopass`, `resetpass` | Add a password, remove one, add one by its SHA-256, allow any password, remove them all. |
| `~pattern`, `%R~pattern`, `%W~pattern`, `allkeys`, `resetkeys` | Keys it may read and write, only read, only write, any key, none. |
| `&pattern`, `allchannels`, `resetchannels` | Pub/Sub channels it may use. |
| `+@category`, `-@category`, `+command`, `-command`, `+command\|sub` | Commands it may run, by [category](../commands/acl-cat.md) or one by one. |
| `readonly` | No write commands: `-@write`. |
| `(...)`, `clearselectors` | Selectors: another set of keys and commands that also applies. |
| `reset` | Back to a user with no rights. |

[`ACL DRYRUN`](../commands/acl-dryrun.md) says whether a user may run a command, without running it; [`ACL LOG`](../commands/acl-log.md) lists recent refusals and failed logins.

### Keeping users

Users made with `ACL SETUSER` are kept in memory only. To keep them across restarts, start the server with an [`aclfile`](../reference/configuration.md#aclfile), and write them to it with [`ACL SAVE`](../commands/acl-save.md); `ACL SETUSER` does not write it. [`ACL LOAD`](../commands/acl-load.md) reads the file again, and replaces every user with it. The file has a `user name rules...` line for each:

```
user default on #5fcf82bc... ~* &* +@all
user app on #2a4cdf0b... ~app:* resetchannels -@all +@read +@write -@dangerous
```

Users are not replicated, and every node of a cluster has its own: give every node the same file. A replica logs in to its master with [`masterauth`](../reference/configuration.md#masterauth) and [`masteruser`](../reference/configuration.md#masteruser).

### Changing a password

A client already logged in stays logged in when the password it used changes, or is removed. One whose user is turned `off` stays connected and is refused every command; one whose user is deleted is disconnected.

## What clients may do

Even a user that may write everything should not need the commands that run the server. The `@dangerous` category has them: `CONFIG`, `FLUSHALL` and `FLUSHDB`, `KEYS`, `DEBUG`, `SHUTDOWN`, `MONITOR`, `ACL`, `CLIENT KILL`, the cluster administration commands, and others. Give applications `+@all -@dangerous`, or narrower rights, and keep the `default` user, or one with `+@all`, for administration.

There is no `rename-command`: ACL rules are how commands are kept from clients. [`DEBUG SLEEP`](../commands/debug.md) blocks a thread of the server for as long as it is told.

A script's commands are checked against the rights of the user that runs it. In builds with Lua, scripts run in a sandbox: no files, no network, no `os` but the clock, no loading of compiled code.

## TLS

In builds with TLS (`tls` and `full`), the server accepts TLS connections on [`tls-port`](../reference/configuration.md#tls-port), with [`tls-cert-file`](../reference/configuration.md#tls-cert-file) and [`tls-key-file`](../reference/configuration.md#tls-key-file):

```
kividb --tls-port 6390 --tls-cert-file /etc/kividb/tls/server.crt \
  --tls-key-file /etc/kividb/tls/server.key --tls-ca-cert-file /etc/kividb/tls/ca.crt
```

TLS 1.2 and 1.3 are accepted. The plain port stays open beside it: keep it to the local machine with a firewall. With [`tls-ca-cert-file`](../reference/configuration.md#tls-ca-cert-file), clients must present a certificate signed by that CA; [`tls-auth-clients`](../reference/configuration.md#tls-auth-clients) `optional` lets them choose. A certificate lets a client connect; it still logs in with `AUTH`.

Between servers: [`tls-replication`](../reference/configuration.md#tls-replication) makes replicas connect to their master over TLS, and [`tls-cluster`](../reference/configuration.md#tls-cluster) the cluster's nodes to each other. Each node presents a certificate and checks the other's against the CA; the host name in it is not checked, as in Redis.

### Known issue

Certificates are read when the server starts. `CONFIG SET tls-cert-file` replies `OK` and changes nothing: renewed certificates take a restart. Filed as [kividb#156](https://github.com/kividbio/kividb/issues/156).

## The cluster bus

Anything that can reach a node's bus port can join the cluster, as in Redis. Give every node the same [`cluster-bus-secret`](../reference/configuration.md#cluster-bus-secret): a node connecting to another must then answer a challenge with it, an HMAC-SHA256, before anything it sends is read, and the secret itself is never sent. [`cluster-bus-port-protected-mode yes`](../reference/configuration.md#cluster-bus-port-protected-mode) refuses to start a node without one. The bus is not encrypted without `tls-cluster`.

## The update check

At startup the server asks GitHub, over HTTPS, for the newest release, and logs a line if it is newer than itself. The request carries the server's version and nothing else. `--update-check no`, or the environment variable `KIVIDB_NO_UPDATE_CHECK=1`, turns it off.

## Known issue

While the `default` user has no password, `AUTH` with any password replies `OK`; Redis replies with an error. Filed as [kividb#135](https://github.com/kividbio/kividb/issues/135).

## Reporting a vulnerability

Report it privately, as [SECURITY.md](https://github.com/kividbio/kividb/blob/master/SECURITY.md) says, not in a public issue.
