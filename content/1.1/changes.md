---
title: "What changed"
description: "What each release of KiviDB 1.1 added, removed and changed."
version: "1.1"
weight: 90
---

What each release added, removed and changed in the commands and settings, as each release's server reports them. The [changelog](https://github.com/kividbio/kividb/blob/master/CHANGELOG.md) says why.

## 1.1.3

A security release: it fixes [GHSA-58x5-jq4h-h6rr](https://github.com/kividbio/kividb/security/advisories/GHSA-58x5-jq4h-h6rr) (a TLS client that does not finish its handshake holds up the others), [GHSA-rhrj-pgm8-2686](https://github.com/kividbio/kividb/security/advisories/GHSA-rhrj-pgm8-2686) (writes to a key past its time to live are lost) and [GHSA-pjrr-m43f-m5g3](https://github.com/kividbio/kividb/security/advisories/GHSA-pjrr-m43f-m5g3) (overlapping AOF checkpoints, or a crash during one, lose acknowledged writes), and the other bugs its [changelog](https://github.com/kividbio/kividb/blob/v1.1.3/CHANGELOG.md) lists. [`maxclients`](reference/configuration.md#maxclients) is now enforced, and taken in the configuration file. **Upgrade the replicas first, then their master** ([Replication](guides/replication.md#upgrading)).

No change to the commands or settings.

## 1.1.2

No change to the commands or settings.

## 1.1.1

**Withdrawn.** Under a high rate of writes with a TTL, background expiry falls behind and memory grows without bound ([#87](https://github.com/kividbio/kividb/issues/87)). Use 1.1.2 or later: patch releases of 1.1.0 that include everything in 1.1.1 and the fix. The 1.1.1 images and packages are still published, so that a pinned deployment does not break.

**New commands:** [`XIDMPRECORD`](commands/xidmprecord.md)

**New settings:** `array-slice-size`, `array-sparse-kmax`, `array-sparse-kmin`, `key-access-tracking`

## 1.1.0

The first release these docs cover: every command and setting in it is “since 1.1.0”.
