---
title: "What changed"
description: "What each release of KiviDB 1.1 added, removed and changed."
version: "1.1"
weight: 90
---

What each release added, removed and changed in the commands and settings, as each release's server reports them. The [changelog](https://github.com/kividbio/kividb/blob/master/CHANGELOG.md) says why.

## 1.1.2

No change to the commands or settings.

## 1.1.1

**Withdrawn.** Under a high rate of writes with a TTL, background expiry falls behind and memory grows without bound ([#87](https://github.com/kividbio/kividb/issues/87)). Use 1.1.2, a patch release of 1.1.0 that includes everything in 1.1.1 and the fix. The 1.1.1 images and packages are still published, so that a pinned deployment does not break.

**New commands:** [`XIDMPRECORD`](commands/xidmprecord.md)

**New settings:** `array-slice-size`, `array-sparse-kmax`, `array-sparse-kmin`, `key-access-tracking`

## 1.1.0

The first release these docs cover: every command and setting in it is “since 1.1.0”.
