---
title: "Install KiviDB"
description: "Run the KiviDB 1.2 release candidate from a Docker image, a Linux binary or package, or build it from source."
version: "1.2"
weight: 10
---

**KiviDB 1.2.0 has not been released.** What is published is its release candidate, `v1.2.0-rc3`, for testing. Use [1.1.3](../../1.1/get-started/install.md) in production until 1.2.0 is out, and read [Upgrading from 1.1](upgrading.md) before you try 1.2 on data you keep.

The release candidate is published as Docker images, and as Linux binaries and `.deb` and `.rpm` packages. Each comes in four builds; the default one fits most uses. See [Choose a build](builds.md).

## Docker

Images are on the GitHub Container Registry and Docker Hub (`kividb/kividb`), with the same tags in both:

```bash
docker run -d -p 6380:6380 ghcr.io/kividbio/kividb:v1.2.0-rc3
# or
docker run -d -p 6380:6380 kividb/kividb:v1.2.0-rc3
```

| Tag | Build |
|---|---|
| `v1.2.0-rc3` | default |
| `v1.2.0-rc3-lua` | with Lua scripting |
| `v1.2.0-rc3-tls` | with TLS |
| `v1.2.0-rc3-full` | Lua and TLS |

Images are built for `amd64` and `arm64`. A release candidate never moves `latest` or `1.1`: those stay on the newest release, 1.1.3, until 1.2.0 is released.

**Arguments replace the image's default command.** A container is always reached through its network, never over loopback, so the image runs with `--protected-mode no` by default. Any arguments you pass replace that, and protected mode is on again. When you pass your own flags, set a password, or add `--protected-mode no` yourself:

```bash
docker run -d -p 6380:6380 ghcr.io/kividbio/kividb:v1.2.0-rc3 --requirepass "change-me"
```

**Keeping data.** Mount a volume on `/home/kividb`, where the server runs as UID 1000. With `--aof`, every write is also appended to a log that is replayed on start:

```bash
docker run -d -p 6380:6380 -v "$(pwd)/data:/home/kividb" \
  ghcr.io/kividbio/kividb:v1.2.0-rc3 --aof --requirepass "change-me"
```

The image has no shell, no `redis-cli`, and, since 1.2, no OpenSSL either (TLS is built into the binary). Connect from another container, for example:

```bash
docker run --rm -it --network container:<name> redis redis-cli -p 6380
```

**io_uring.** On Linux, KiviDB uses io_uring when the kernel allows it, and Tokio otherwise. Docker's default seccomp profile blocks io_uring, so in a container KiviDB uses Tokio unless you run it with `--security-opt seccomp=unconfined`. Understand what that allows before you use it in production.

## Linux binaries and packages

A release candidate has no GitHub release. Its Linux binaries, packages and checksums are pushed to the GitHub Container Registry beside its images, as one artifact, `ghcr.io/kividbio/kividb-binaries:v1.2.0-rc3`. Download it with the [ORAS](https://oras.land) command-line tool; no login is needed:

```bash
oras pull ghcr.io/kividbio/kividb-binaries:v1.2.0-rc3
sha256sum -c SHA256SUMS.txt
tar xzf kividb-linux-x86_64.tar.gz
./kividb/kividb
```

That downloads every file of the release candidate:

| System | Files |
|---|---|
| Linux x86_64 | `kividb-linux-x86_64.tar.gz`, `kividb-lua-…`, `kividb-tls-…`, `kividb-full-linux-x86_64.tar.gz` |
| Linux aarch64 | `kividb-linux-aarch64.tar.gz`, `kividb-lua-…`, `kividb-tls-…`, `kividb-full-linux-aarch64.tar.gz` |
| Debian, Ubuntu | `kividb_amd64.deb`, `kividb_arm64.deb` |
| RHEL, Fedora | `kividb.x86_64.rpm`, `kividb.aarch64.rpm` |

There are no macOS binaries of a release candidate: on a Mac, use Docker, or build it from source. The Linux aarch64 binary needs an ARMv8.1 CPU or newer: AWS Graviton2 and later, or Ampere. It does not run on a Raspberry Pi 4.

The packages are of the default build:

```bash
sudo apt install ./kividb_amd64.deb
# or
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
gh attestation verify oci://ghcr.io/kividbio/kividb:v1.2.0-rc3 --repo kividbio/kividb
```

## From source

You need a stable Rust toolchain, 1.89 or newer:

```bash
git clone https://github.com/kividbio/kividb.git
cd kividb
git checkout v1.2.0-rc3

cargo build --release                      # default build
cargo build --release --features lua       # with Lua scripting
cargo build --release --features tls       # with TLS
cargo build --release --features lua,tls   # both

./target/release/kividb
```

`docker build -t kividb .` builds the default image. `docker build --build-arg KIVIDB_FEATURES=lua,tls -t kividb:full .` builds another build.

## Next

[Quick start](quick-start.md): connect and store some data.
