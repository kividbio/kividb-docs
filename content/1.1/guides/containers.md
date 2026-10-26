---
title: "Docker and Kubernetes"
description: "Run KiviDB in containers: the image, keeping data, memory, stopping cleanly, health checks, io_uring, and Kubernetes."
version: "1.1"
weight: 70
---

The image is `kividb/kividb` on Docker Hub, or `ghcr.io/kividbio/kividb`, for `amd64` and `arm64`; [Install](../get-started/install.md#docker) lists its tags. Pin a version tag, `v1.1.2`, not `latest`.

## What the image is

- The server runs as user and group 1000, in `/home/kividb`, its working directory: snapshots, the append-only file, backups and `nodes.conf` are written there.
- It listens on 6380.
- Its default command is `--protected-mode no`, since a container is reached through its network, never its loopback. Arguments given to `docker run`, or `args` in Kubernetes, replace it: protected mode is then on again, and clients from other containers are refused until the server has a password. Give it a password.
- There is no shell, and no `redis-cli`, in the image.

```bash
docker run -d --name kividb -p 6380:6380 \
  -v kividb-data:/home/kividb \
  kividb/kividb:v1.1.2 --requirepass "change-me" --aof --maxmemory 1gb
```

## Keeping data

Mount a volume on `/home/kividb`, writable by UID 1000. Without one, the data is gone with the container. With `--aof`, every write goes to the append-only file as well; without it, data is saved only by `SAVE`, `BGSAVE` and a clean stop. See [Persistence](persistence.md).

## Memory

Set [`maxmemory`](../reference/configuration.md#maxmemory) below the container's memory limit. The limit is on the process's resident memory, which is higher than the `used_memory` that `maxmemory` is compared with; leave a quarter or so between them, more for a server with many clients or replicas. A server that reaches the container's limit is killed by the kernel, and loses what was not on disk. See [Memory](memory.md).

## Stopping cleanly

`docker stop` and Kubernetes send `SIGTERM`; the server then saves a snapshot and exits. If it is still saving when the grace period ends, it is killed, and the snapshot is not written. The grace period is 10 seconds in Docker and 30 in Kubernetes. A large dataset takes longer to save: give it time, with `docker stop -t 120`, `--stop-timeout`, or `terminationGracePeriodSeconds`.

## Health checks

Without a shell or a client in the image, check from outside:

- **Is it up:** a TCP connection to port 6380. In Kubernetes, a `tcpSocket` probe. While the server loads its data at startup, it does not listen yet, so the check fails until it is ready: a large dataset can take minutes.
- **Is it serving:** `PING`, from a client. While a replica loads its master's data, commands get `LOADING`.
- **Is a replica following:** `master_link_status:up` in `INFO replication`.

In Kubernetes, give the load time with a startup probe, so that the liveness probe does not restart a server that is still loading:

```yaml
startupProbe:
  tcpSocket:
    port: 6380
  periodSeconds: 5
  failureThreshold: 120   # up to 10 minutes to load
readinessProbe:
  tcpSocket:
    port: 6380
  periodSeconds: 5
livenessProbe:
  tcpSocket:
    port: 6380
  periodSeconds: 10
```

To use `redis-cli` against a container:

```bash
docker run --rm -it --network container:kividb redis redis-cli -p 6380 -a change-me
```

## io_uring

On Linux, KiviDB uses io_uring when the kernel allows it, which is faster, and Tokio otherwise. Docker's default seccomp profile blocks io_uring, and so does Kubernetes's `RuntimeDefault` profile, so there it uses Tokio. `--security-opt seccomp=unconfined` lets it use io_uring; understand what that allows before using it in production. [`io-model`](../reference/configuration.md#io-model) chooses one.

## CPU

The server starts a thread for each CPU it may use, less two when there are four or more; on Linux, a container's CPU limit counts. Set [`threads`](../reference/configuration.md#threads) to choose.

## Replicas and clusters in containers

The address a node is seen at from another container, or another pod, is not always the one to reach it at. Announce the one to use:

- a replica: [`replica-announced-port`](../reference/configuration.md#replica-announced-port), for the port its master lists;
- a cluster node: [`cluster-announce-ip`](../reference/configuration.md#cluster-announce-ip), or [`cluster-announce-hostname`](../reference/configuration.md#cluster-announce-hostname), and the ports. In Kubernetes, a StatefulSet's stable host names, with `cluster-preferred-endpoint-type hostname`, keep working when pods move.

Each cluster node keeps `nodes.conf` in its volume, with its ID and the cluster's shape; a node that loses it joins as a new node. See [Cluster](cluster.md).

## Kubernetes

[kividb-operator](https://github.com/kividbio/kividb-operator) runs KiviDB on Kubernetes: a master and replicas with failover, or a sharded cluster, with backups. Without it, run each server as a StatefulSet with a volume claim, a Service for clients, and the probes and grace period above.
