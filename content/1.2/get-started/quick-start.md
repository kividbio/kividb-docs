---
title: "Quick start"
description: "Start the KiviDB 1.2 release candidate, connect with redis-cli or a client library, and store and read data."
version: "1.2"
weight: 20
---

These steps use the release candidate, `v1.2.0-rc3`: 1.2.0 has not been released. For production, use [1.1.3](../../1.1/get-started/quick-start.md).

## Start the server

With Docker:

```bash
docker run -d --name kividb -p 6380:6380 ghcr.io/kividbio/kividb:v1.2.0-rc3
```

Or with a [Linux binary](install.md#linux-binaries-and-packages):

```bash
./kividb/kividb
```

KiviDB listens on **port 6380**, on every address, with [protected mode](#protected-mode) on.

## Connect

Any Redis client works. With `redis-cli`, give the port:

```bash
redis-cli -p 6380
```

```
127.0.0.1:6380> PING
PONG
```

## Store and read data

Strings, with a counter and an expiry:

```
127.0.0.1:6380> SET greeting hello
OK
127.0.0.1:6380> GET greeting
"hello"
127.0.0.1:6380> EXPIRE greeting 60
(integer) 1
127.0.0.1:6380> TTL greeting
(integer) 60
127.0.0.1:6380> SET counter 10
OK
127.0.0.1:6380> INCR counter
(integer) 11
```

A hash:

```
127.0.0.1:6380> HSET user:1 name Ada lang Rust
(integer) 2
127.0.0.1:6380> HGETALL user:1
1) "name"
2) "Ada"
3) "lang"
4) "Rust"
```

Search is built in, with no module to load. An index over hashes, and a query that finds a word by its other forms:

```
127.0.0.1:6380> FT.CREATE idx ON HASH PREFIX 1 doc: SCHEMA body TEXT
OK
127.0.0.1:6380> HSET doc:1 body "I prefer email"
(integer) 1
127.0.0.1:6380> FT.SEARCH idx "preferences" NOCONTENT
1) (integer) 1
2) "doc:1"
```

See [Commands](../commands/index.md) for every command, and [Search](../guides/search.md) for what an index can hold.

## From an application

Use the Redis client library of your language, and point it at port 6380. In Python, with `redis-py`:

```python
import redis

r = redis.Redis(host="localhost", port=6380)
r.set("greeting", "hello")
print(r.get("greeting"))  # b'hello'
```

In Node.js, with `ioredis`:

```js
import Redis from "ioredis";

const redis = new Redis({ host: "localhost", port: 6380 });
await redis.set("greeting", "hello");
console.log(await redis.get("greeting")); // hello
```

See [Client libraries](clients.md) for others.

## Protected mode

Protected mode is on by default, as in Redis. While it is on, and as long as no bind address has been set and the `default` user has no password, only clients on the same machine can connect. Others get a `-DENIED` error that explains what to do, and are disconnected.

To let other machines connect, do one of these:

- set a password: `--requirepass <password>`, or `ACL SETUSER default ><password>`;
- set a bind address: `--bind <address>`;
- turn protected mode off: `--protected-mode no`, or `CONFIG SET protected-mode no` from a local client.

Before you turn it off, or bind to an address the internet can reach, set a password.

The Docker image starts with `--protected-mode no`, since a container is never reached over loopback. Arguments you pass replace that: see [Install KiviDB](install.md#docker).

## Next

- [Choose a build](builds.md), if you need Lua scripting or TLS.
- [Upgrading from 1.1](upgrading.md), if you run 1.1 now.
- [Configuration](../reference/configuration.md): every setting.
