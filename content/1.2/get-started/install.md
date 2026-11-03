---
title: "Install KiviDB"
description: "Run KiviDB 1.2 from a Docker image, a release binary, Homebrew, a Linux package, or build it from source."
version: "1.2"
weight: 10
---

KiviDB 1.2 is published as Docker images, as binaries for Linux and macOS, as a Homebrew formula, and as `.deb` and `.rpm` packages. Each comes in four builds; the default one fits most uses. See [Choose a build](builds.md).

Coming from 1.1? Read [Upgrading from 1.1](upgrading.md) first.

## Docker

Images are on the GitHub Container Registry and Docker Hub (`kividb/kividb`), with the same tags in both:

```bash
docker run -d -p 6380:6380 ghcr.io/kividbio/kividb:v1.2.0
# or
docker run -d -p 6380:6380 kividb/kividb:v1.2.0
```

| Tag | Build |
|---|---|
| `v1.2.0`, `1.2`, `latest` | default |
| `v1.2.0-lua` | with Lua scripting |
| `v1.2.0-tls` | with TLS |
| `v1.2.0-full` | Lua and TLS |

Images are built for `amd64` and `arm64`. `latest` is the newest release; pin a version tag in production.

**Arguments replace the image's default command.** A container is always reached through its network, never over loopback, so the image runs with `--protected-mode no` by default. Any arguments you pass replace that, and protected mode is on again. When you pass your own flags, set a password, or add `--protected-mode no` yourself:

```bash
docker run -d -p 6380:6380 ghcr.io/kividbio/kividb:v1.2.0 --requirepass "change-me"
```

**Keeping data.** Mount a volume on `/home/kividb`, where the server runs as UID 1000. With `--aof`, every write is also appended to a log that is replayed on start:

```bash
docker run -d -p 6380:6380 -v "$(pwd)/data:/home/kividb" \
  ghcr.io/kividbio/kividb:v1.2.0 --aof --requirepass "change-me"
```

Give each server a volume of its own: a second server started on a data directory another one is using waits until the first has stopped. See [Persistence](../guides/persistence.md#one-server-per-data-directory).

The image has no shell, no `redis-cli`, and, since 1.2, no OpenSSL either (TLS is built into the binary). Connect from another container, for example:

```bash
docker run --rm -it --network container:<name> redis redis-cli -p 6380
```

**io_uring.** On Linux, KiviDB uses io_uring when the kernel allows it, and Tokio otherwise. Docker's default seccomp profile blocks io_uring, so in a container KiviDB uses Tokio unless you run it with `--security-opt seccomp=unconfined`. Understand what that allows before you use it in production.

## Release binaries

Binaries for Linux (x86_64, aarch64) and macOS (Apple silicon, Intel) are attached to each [GitHub release](https://github.com/kividbio/kividb/releases):

```bash
curl -LO https://github.com/kividbio/kividb/releases/download/v1.2.0/kividb-linux-x86_64.tar.gz
tar xzf kividb-linux-x86_64.tar.gz
./kividb/kividb
```

| System | File |
|---|---|
| Linux x86_64 | `kividb-linux-x86_64.tar.gz` |
| Linux aarch64 | `kividb-linux-aarch64.tar.gz` |
| macOS, Apple silicon | `kividb-darwin-aarch64.tar.gz` |
| macOS, Intel | `kividb-darwin-x86_64.tar.gz` |

The other builds have their name in the file: `kividb-lua-linux-x86_64.tar.gz`, `kividb-tls-…`, `kividb-full-…`. `SHA256SUMS.txt` in each release lists every file's checksum.

The Linux aarch64 binary needs an ARMv8.1 CPU or newer: AWS Graviton2 and later, or Ampere. It does not run on a Raspberry Pi 4.

## Homebrew

On macOS, the default build installs with:

```bash
brew install kividbio/tap/kividb
kividb --version
```

## Linux packages

Each release has `.deb` and `.rpm` packages of the default build, for `amd64` and `arm64`:

```bash
curl -LO https://github.com/kividbio/kividb/releases/download/v1.2.0/kividb_amd64.deb
sudo apt install ./kividb_amd64.deb
# or
curl -LO https://github.com/kividbio/kividb/releases/download/v1.2.0/kividb.x86_64.rpm
sudo rpm -i kividb.x86_64.rpm
```

A package installs the binary, a systemd unit, a `kividb` system user, and `/etc/kividb/kividb.conf`, which listens on loopback only. Installing starts the service, and upgrading restarts it.

- Data (snapshots, the AOF, `nodes.conf`) is in `/var/lib/kividb`.
- Logs go to the journal: `journalctl -u kividb`.
- To accept clients from other machines, set a password and change `bind` in `/etc/kividb/kividb.conf`.

To upgrade servers that replicate, upgrade the replicas first and their master last. See [Upgrading from 1.1](upgrading.md).

## Checking what you downloaded

`SHA256SUMS.txt` shows that a file arrived whole. Since 1.2, every file and image also carries a signed build attestation, which shows that it was built by KiviDB's release workflow from the tagged commit. Check one with the GitHub CLI:

```bash
gh attestation verify kividb-linux-x86_64.tar.gz --repo kividbio/kividb
gh attestation verify oci://ghcr.io/kividbio/kividb:v1.2.0 --repo kividbio/kividb
```

## From source

You need a stable Rust toolchain, 1.89 or newer:

```bash
git clone https://github.com/kividbio/kividb.git
cd kividb
git checkout v1.2.0

cargo build --release                      # default build
cargo build --release --features lua       # with Lua scripting
cargo build --release --features tls       # with TLS
cargo build --release --features lua,tls   # both

./target/release/kividb
```

`docker build -t kividb .` builds the default image. `docker build --build-arg KIVIDB_FEATURES=lua,tls -t kividb:full .` builds another build.

## Next

[Quick start](quick-start.md): connect and store some data.
