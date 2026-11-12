---
title: "What changed"
description: "What each release of KiviDB 1.2 added, removed and changed."
version: "1.2"
weight: 90
---

What each release added, removed and changed in the commands and settings, as each release's server reports them. The [changelog](https://github.com/kividbio/kividb/blob/master/CHANGELOG.md) says why.

## 1.2.2

Released on 13 November 2026, a patch release of 1.2.1 that fixes one security issue: [GHSA-8rm8-p5c5-g3mr](https://github.com/kividbio/kividb/security/advisories/GHSA-8rm8-p5c5-g3mr) (a multi-key write over a key past its time to live, with `MSET`, `MSETNX`, `JSON.MSET`, or a `MULTI`/`EXEC` of plain `SET`s after `WATCH`, could make the server stop answering, until a restart, when a search index existed and was being changed at the same time). Servers without a search index, and 1.1, were not affected. Nothing else changes. **Upgrade from 1.2.x, the replicas first, then their master**: [Upgrading from 1.2.1 to 1.2.2](get-started/upgrading.md#upgrading-from-121-to-122).

No change to the commands or settings.

## 1.2.1

Released on 12 November 2026, a patch release of 1.2.0. It fixes two security issues: [GHSA-cg4w-p5w5-57w5](https://github.com/kividbio/kividb/security/advisories/GHSA-cg4w-p5w5-57w5) (commands that write only with some arguments, such as `GEORADIUS ... STORE` and `MIGRATE`, got past read-only ACL key permissions and the `@read` and `@write` categories, and were not held by `min-replicas-to-write`, the out-of-memory refusal or `aof-ack-after-write`) and [GHSA-qh83-449g-hwm5](https://github.com/kividbio/kividb/security/advisories/GHSA-qh83-449g-hwm5) (a deeply nested JSON document could crash the server). It also fixes the 1.2.0 known issues of reshards that could lose writes and replicas that could stop while they saved. **Upgrade the replicas first, then their master**: [Upgrading from 1.2.0 to 1.2.1](get-started/upgrading.md#upgrading-from-120-to-121) says what you will notice.

**New commands:** [`DEBUG DIGEST-VALUE`](commands/debug-digest-value.md), [`DEBUG HELP`](commands/debug-help.md), [`DEBUG LOG`](commands/debug-log.md), [`DEBUG OBJECT`](commands/debug-object.md), [`DEBUG PAUSE-CRON`](commands/debug-pause-cron.md), [`DEBUG POPULATE`](commands/debug-populate.md), [`DEBUG PROTOCOL`](commands/debug-protocol.md), [`DEBUG SET-ACTIVE-EXPIRE`](commands/debug-set-active-expire.md), [`DEBUG SET-DISABLE-DENY-SCRIPTS`](commands/debug-set-disable-deny-scripts.md), [`DEBUG SLEEP`](commands/debug-sleep.md)

**Commands changed:** [`ACL`](commands/acl.md), [`ASKING`](commands/asking.md), [`BACKUP`](commands/backup.md), [`BGREWRITEAOF`](commands/bgrewriteaof.md), [`BGSAVE`](commands/bgsave.md), [`CLUSTER`](commands/cluster.md), [`COMMAND`](commands/command.md), [`CONFIG`](commands/config.md), [`COPY`](commands/copy.md), [`DBSIZE`](commands/dbsize.md), [`DEBUG`](commands/debug.md), [`DEL`](commands/del.md), [`DUMP`](commands/dump.md), [`EXISTS`](commands/exists.md), [`EXPIRE`](commands/expire.md), [`EXPIREAT`](commands/expireat.md), [`EXPIRETIME`](commands/expiretime.md), [`FAILOVER`](commands/failover.md), [`FLUSHALL`](commands/flushall.md), [`FLUSHDB`](commands/flushdb.md), [`GEORADIUS`](commands/georadius.md), [`GEORADIUSBYMEMBER`](commands/georadiusbymember.md), [`HOTKEYS`](commands/hotkeys.md), [`INFO`](commands/info.md), [`JSON.ARRAPPEND`](commands/json.arrappend.md), [`JSON.ARRINDEX`](commands/json.arrindex.md), [`JSON.ARRINSERT`](commands/json.arrinsert.md), [`JSON.ARRTRIM`](commands/json.arrtrim.md), [`JSON.MERGE`](commands/json.merge.md), [`JSON.MGET`](commands/json.mget.md), [`JSON.MSET`](commands/json.mset.md), [`JSON.NUMINCRBY`](commands/json.numincrby.md), [`JSON.NUMMULTBY`](commands/json.nummultby.md), [`JSON.SET`](commands/json.set.md), [`JSON.STRAPPEND`](commands/json.strappend.md), [`JSON.TOGGLE`](commands/json.toggle.md), [`KEYS`](commands/keys.md), [`LASTSAVE`](commands/lastsave.md), [`LATENCY`](commands/latency.md), [`LOLWUT`](commands/lolwut.md), [`MEMORY`](commands/memory.md), [`MIGRATE`](commands/migrate.md), [`MODULE`](commands/module.md), [`MONITOR`](commands/monitor.md), [`MOVE`](commands/move.md), [`OBJECT`](commands/object.md), [`PERSIST`](commands/persist.md), [`PEXPIRE`](commands/pexpire.md), [`PEXPIREAT`](commands/pexpireat.md), [`PEXPIRETIME`](commands/pexpiretime.md), [`PSYNC`](commands/psync.md), [`PTTL`](commands/pttl.md), [`RANDOMKEY`](commands/randomkey.md), [`READONLY`](commands/readonly.md), [`READWRITE`](commands/readwrite.md), [`RENAME`](commands/rename.md), [`RENAMENX`](commands/renamenx.md), [`REPLCONF`](commands/replconf.md), [`REPLICAOF`](commands/replicaof.md), [`RESTORE`](commands/restore.md), [`ROLE`](commands/role.md), [`SAVE`](commands/save.md), [`SCAN`](commands/scan.md), [`SELECT`](commands/select.md), [`SHUTDOWN`](commands/shutdown.md), [`SLAVEOF`](commands/slaveof.md), [`SLOWLOG`](commands/slowlog.md), [`SORT`](commands/sort.md), [`SORT_RO`](commands/sort_ro.md), [`SWAPDB`](commands/swapdb.md), [`SYNC`](commands/sync.md), [`TIME`](commands/time.md), [`TOUCH`](commands/touch.md), [`TTL`](commands/ttl.md), [`TYPE`](commands/type.md), [`UNLINK`](commands/unlink.md), [`WAIT`](commands/wait.md), [`WAITAOF`](commands/waitaof.md)

**New settings:** `acllog-max-len`, `replica-announced`, `replica-priority`, `slave-priority`

## 1.2.0

Released on 3 November 2026. It fixes two security issues that affect 1.1.3: [GHSA-6rw7-4fcr-r6j3](https://github.com/kividbio/kividb/security/advisories/GHSA-6rw7-4fcr-r6j3) (ACL key permissions bypassed through `SORT` patterns and multi-`STORE` destinations) and [GHSA-c4xj-63wm-4jj9](https://github.com/kividbio/kividb/security/advisories/GHSA-c4xj-63wm-4jj9) (credentials in `SLOWLOG`, `MONITOR` and the log). 1.1 gets no further release. [Upgrading from 1.1](get-started/upgrading.md#upgrading-from-11-to-12) says what to check before upgrading, and in what order.

**Commands removed:** `GEODELBYMEMBER`

**Commands changed:** [`PFDEBUG`](commands/pfdebug.md)

**New settings:** `active-defrag-cycle-max`, `active-defrag-ignore-bytes`, `active-defrag-threshold-lower`, `aof-ack-after-write`, `cluster-announce-client-port`, `cluster-replica-validity-factor`, `hll-write-format`, `latency-monitor-threshold`, `repl-replica-sync-max-backlog-bytes`, `search-min-stem-len`, `search-on-timeout`, `search-timeout`, `shutdown-timeout`, `tls-auth-clients-allowed-names`, `ts-duplicate-policy`

**Defaults changed:** `activedefrag`, `lazyfree-lazy-user-del`, `repl-backlog-size`
