---
title: "What changed"
description: "What each release of KiviDB 1.2 added, removed and changed."
version: "1.2"
weight: 90
---

What each release added, removed and changed in the commands and settings, as each release's server reports them. The [changelog](https://github.com/kividbio/kividb/blob/master/CHANGELOG.md) says why.

## 1.2.0

Released on 3 November 2026. It fixes two security issues that affect 1.1.3: [GHSA-6rw7-4fcr-r6j3](https://github.com/kividbio/kividb/security/advisories/GHSA-6rw7-4fcr-r6j3) (ACL key permissions bypassed through `SORT` patterns and multi-`STORE` destinations) and [GHSA-c4xj-63wm-4jj9](https://github.com/kividbio/kividb/security/advisories/GHSA-c4xj-63wm-4jj9) (credentials in `SLOWLOG`, `MONITOR` and the log). 1.1 gets no further release. [Upgrading from 1.1](get-started/upgrading.md) says what to check before upgrading, and in what order.

**Commands removed:** `GEODELBYMEMBER`

**Commands changed:** [`PFDEBUG`](commands/pfdebug.md)

**New settings:** `active-defrag-cycle-max`, `active-defrag-ignore-bytes`, `active-defrag-threshold-lower`, `aof-ack-after-write`, `cluster-announce-client-port`, `cluster-replica-validity-factor`, `hll-write-format`, `latency-monitor-threshold`, `repl-replica-sync-max-backlog-bytes`, `search-min-stem-len`, `search-on-timeout`, `search-timeout`, `shutdown-timeout`, `tls-auth-clients-allowed-names`, `ts-duplicate-policy`

**Defaults changed:** `activedefrag`, `lazyfree-lazy-user-del`, `repl-backlog-size`
