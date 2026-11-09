---
title: "PUBSUB"
description: "Reports on the channels and patterns clients are subscribed to."
version: "1.2"
command: "PUBSUB"
syntax: "PUBSUB"
group: "pub-sub"
since: "1.1.0"
arity: -2
flags: ["pubsub"]
acl_categories: ["pubsub", "slow"]
history: []
subcommands: ["PUBSUB CHANNELS", "PUBSUB HELP", "PUBSUB NUMPAT", "PUBSUB NUMSUB", "PUBSUB SHARDCHANNELS", "PUBSUB SHARDNUMSUB"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PUBSUB
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`

Subcommands: [PUBSUB CHANNELS](pubsub-channels.md), [PUBSUB HELP](pubsub-help.md), [PUBSUB NUMPAT](pubsub-numpat.md), [PUBSUB NUMSUB](pubsub-numsub.md), [PUBSUB SHARDCHANNELS](pubsub-shardchannels.md), [PUBSUB SHARDNUMSUB](pubsub-shardnumsub.md)
<!-- generated: end -->
`PUBSUB` is a container: its subcommands report on the channels and patterns clients are subscribed to. They do not subscribe or publish anything, and they count only the clients connected to the server that answers; in a cluster, each node reports its own.

| Subcommand | |
|---|---|
| [`PUBSUB CHANNELS`](pubsub-channels.md) | the channels with subscribers, optionally those matching a pattern |
| [`PUBSUB NUMSUB`](pubsub-numsub.md) | how many clients are subscribed to each of some channels |
| [`PUBSUB NUMPAT`](pubsub-numpat.md) | how many distinct patterns are subscribed to |
| [`PUBSUB SHARDCHANNELS`](pubsub-shardchannels.md), [`PUBSUB SHARDNUMSUB`](pubsub-shardnumsub.md) | the same for shard channels |
| [`PUBSUB HELP`](pubsub-help.md) | the list, from the server |

[Pub/Sub](../guides/pub-sub.md) explains channels, patterns, shard channels and delivery. `PUBSUB` alone, or with a name that is not a subcommand, is an error.

## Examples

```
> PUBSUB
(error) ERR wrong number of arguments for 'pubsub' command
> PUBSUB NOPE
(error) ERR unknown PUBSUB subcommand 'NOPE'
> PUBSUB NUMSUB news
1) "news"
2) (integer) 1
```
