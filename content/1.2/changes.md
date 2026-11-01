---
title: "What changed"
description: "What each release of KiviDB 1.2 added, removed and changed."
version: "1.2"
weight: 90
---

What each release added, removed and changed in the commands and settings, as each release's server reports them. The [changelog](https://github.com/kividbio/kividb/blob/master/CHANGELOG.md) says why.

## 1.2.0

Not released yet: these pages describe the release candidate, `v1.2.0-rc3`. Use [1.1.3](../1.1/index.md) in production until 1.2.0 is out. [Upgrading from 1.1](get-started/upgrading.md) says what to check before upgrading, and in what order, and what is [known in 1.2.0-rc3](get-started/upgrading.md#known-in-120-rc3).

**Commands removed:** `GEODELBYMEMBER`

**Commands changed:** [`PFDEBUG`](commands/pfdebug.md)

**New settings:** `active-defrag-cycle-max`, `active-defrag-ignore-bytes`, `active-defrag-threshold-lower`, `aof-ack-after-write`, `cluster-announce-client-port`, `cluster-replica-validity-factor`, `hll-write-format`, `latency-monitor-threshold`, `search-min-stem-len`, `search-on-timeout`, `search-timeout`, `tls-auth-clients-allowed-names`, `ts-duplicate-policy`

**Defaults changed:** `activedefrag`, `lazyfree-lazy-user-del`
