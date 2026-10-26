---
title: "Client libraries"
description: "Connect to KiviDB from an application with an ordinary Redis client: which ones have been tried, and how to connect each."
version: "1.1"
weight: 40
---

KiviDB speaks the Redis protocol, RESP2 and RESP3, so an application connects with a Redis client library, unchanged; there is no KiviDB driver. Point it at port 6380, KiviDB's default, and give it the password if there is one.

These were run against KiviDB 1.1.2, each with strings, expiry, hashes, a pipeline and a transaction, and the noted extras:

| Language | Library | Version tried | Also tried |
|---|---|---|---|
| Python | [redis-py](https://github.com/redis/redis-py) | 8.0.1 | Vector and full-text search (`FT.CREATE`, KNN with a tag filter) |
| Node.js | [ioredis](https://github.com/redis/ioredis) | 5.11.1 | Pub/Sub |
| Node.js | [BullMQ](https://bullmq.io) | 5.81.5 | A queue and a worker. Needs a build with Lua. |
| Go | [go-redis](https://github.com/redis/go-redis) | 9.23.0 | |

The examples are in the KiviDB repository, under [`examples/clients`](https://github.com/kividbio/kividb/tree/master/examples/clients), and check their own results.

## Connecting

**Python**, redis-py:

```python
import redis

r = redis.Redis(host="localhost", port=6380, password="change-me", decode_responses=True)
r.set("greeting", "hello")
```

**Node.js**, ioredis:

```javascript
import Redis from "ioredis";

const redis = new Redis({ host: "localhost", port: 6380, password: "change-me" });
await redis.set("greeting", "hello");
```

**Go**, go-redis:

```go
rdb := redis.NewClient(&redis.Options{Addr: "localhost:6380", Password: "change-me"})
rdb.Set(ctx, "greeting", "hello", 0)
```

A URL works too, for clients that take one: `redis://:change-me@localhost:6380/0`, or `rediss://` with TLS.

## Clusters

A cluster client, `RedisCluster` in redis-py, `Redis.Cluster` in ioredis, `ClusterClient` in go-redis, connects to any node and finds the others. See [Cluster](../guides/cluster.md).

## Job queues

BullMQ, Sidekiq and most other job queues run Lua scripts: they need the `lua` or `full` build. See [Choose a build](builds.md), and [Scripting](../guides/scripting.md) for how scripts run in KiviDB.
