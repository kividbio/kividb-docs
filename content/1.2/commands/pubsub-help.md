---
title: "PUBSUB HELP"
description: "Lists the PUBSUB subcommands, one line each with its arguments, followed by an indented line saying what it does: CHANNELS, NUMPAT, NUMSUB, SHARDCHANNELS, SHARDNUMSUB and HELP."
version: "1.2"
command: "PUBSUB HELP"
syntax: "PUBSUB HELP"
group: "pub-sub"
since: "1.1.0"
history: []
container: "PUBSUB"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PUBSUB HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the [`PUBSUB`](pubsub.md) subcommands, one line each with its arguments, followed by an indented line saying what it does: `CHANNELS`, `NUMPAT`, `NUMSUB`, `SHARDCHANNELS`, `SHARDNUMSUB` and `HELP`. The text is the server's own summary, useful from a command line; each subcommand has its own page here.

## Reply

An array of status lines.

## Examples

```
> PUBSUB HELP
 1) PUBSUB <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) CHANNELS [<pattern>]
 3)     Return the currently active channels matching a <pattern> (default: '*').
 4) NUMPAT
 5)     Return number of subscriptions to patterns.
...
12) HELP
13)     Print this help.
```
