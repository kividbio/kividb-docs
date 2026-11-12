---
title: "Install KiviDB"
description: "Run KiviDB 1.2 from the apt or dnf repository, a Docker image, a release binary, Homebrew, Cargo, a Linux package, or build it from source."
version: "1.2"
weight: 10
---

KiviDB 1.2 is published in apt and dnf repositories, as Docker images, as binaries for Linux and macOS, as a Homebrew formula, on crates.io, and as `.deb` and `.rpm` packages. Each comes in four builds; the default one fits most uses. See [Choose a build](builds.md). The newest release is 1.2.1, and the examples on this page install it.

Coming from 1.1 or 1.2.0? Read [Upgrading](upgrading.md) first.

## Linux package repositories

From 1.2.1, the signed apt and dnf repositories at `https://packages.kividb.io` have every stable release, for `amd64`/`x86_64` and `arm64`/`aarch64`. A new release is added when it is published, so `apt upgrade` and `dnf upgrade` keep KiviDB current. 1.2.0 is not in them: for it, use the [packages attached to its GitHub release](#linux-packages).

The packages are the default build, without Lua or TLS. For scripts or a TLS listener, use a `-lua`, `-tls` or `-full` image or binary.

They need glibc 2.34 or newer: Debian 12, Ubuntu 22.04, RHEL, Rocky Linux and AlmaLinux 9, Fedora 35, Amazon Linux 2023, or later. On an older system the package manager refuses them. The `arm64` packages need an ARMv8.1 CPU or newer: AWS Graviton2 and later, or Ampere, not a Raspberry Pi 4.

### Debian and Ubuntu (apt)

```bash
sudo apt update && sudo apt install -y ca-certificates curl
sudo install -d -m 0755 /etc/apt/keyrings
curl -fsSL https://packages.kividb.io/kividb.gpg | sudo tee /etc/apt/keyrings/kividb.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/kividb.sources > /dev/null <<'EOF'
Types: deb
URIs: https://packages.kividb.io/deb
Suites: stable
Components: main
Signed-By: /etc/apt/keyrings/kividb.gpg
EOF
sudo apt update && sudo apt install -y kividb
```

Check that the key you downloaded is the [signing key](#the-signing-key): `gpg --show-keys /etc/apt/keyrings/kividb.gpg`.

For tools that read only one-line `.list` files, the same source is:

```bash
echo "deb [signed-by=/etc/apt/keyrings/kividb.gpg] https://packages.kividb.io/deb stable main" \
  | sudo tee /etc/apt/sources.list.d/kividb.list > /dev/null
```

Use one or the other, not both. Both files can also be downloaded, from `https://packages.kividb.io/kividb.sources` and `https://packages.kividb.io/kividb.list`.

### Fedora, RHEL and compatibles, Amazon Linux 2023 (dnf)

```bash
sudo curl -fsSL -o /etc/yum.repos.d/kividb.repo https://packages.kividb.io/kividb.repo
sudo dnf install -y kividb
```

`kividb.repo` turns on both checks: `gpgcheck=1`, the signature on each package, and `repo_gpgcheck=1`, the signature on the repository's metadata. The first install asks to import the key. Check its fingerprint against [the signing key's](#the-signing-key) before you answer yes (`-y` answers for you).

### What the package installs

- `/usr/bin/kividb`.
- A systemd unit, `kividb.service`, which runs the server as the `kividb` system user. Installing enables and starts it, and an upgrade restarts it if it is running.
- `/etc/kividb/kividb.conf`, which listens on `127.0.0.1:6380` only and turns the startup update check off, since the package manager does upgrades. An upgrade keeps your changes to it.
- `/var/lib/kividb`, where the snapshot, the AOF and `nodes.conf` live. Logs go to the journal: `journalctl -u kividb`.

```bash
systemctl status kividb
redis-cli -p 6380 PING
```

To accept clients from other machines, set a password (`requirepass`) and change `bind` in `/etc/kividb/kividb.conf`, then `sudo systemctl restart kividb`. Without systemd, in a container for example, nothing is started: run `kividb` yourself, as the `kividb` user, from `/var/lib/kividb`.

### Upgrading, pinning, going back and removing

```bash
sudo apt update && sudo apt upgrade        # Debian, Ubuntu
sudo dnf upgrade kividb                    # Fedora, RHEL, Amazon Linux
```

The newest 20 releases stay in the repositories, so you can install or go back to one of them:

```bash
apt list -a kividb                                   # the versions on offer
sudo apt install --allow-downgrades kividb=1.2.1     # that version
sudo apt-mark hold kividb                            # and stay on it

dnf list --showduplicates kividb
sudo dnf install kividb-1.2.1                        # or: sudo dnf downgrade kividb
sudo dnf versionlock add kividb                      # needs the versionlock plugin
```

Before you go back to an older release, read [Upgrading](upgrading.md): a newer server can write files an older one cannot read.

`sudo apt remove kividb` (or `sudo dnf remove kividb`) stops and disables the unit and removes the binary and the unit. The `kividb` user and `/var/lib/kividb`, your data, stay, and so does the configuration with apt: `sudo apt purge kividb` removes it too.

### The signing key

The apt metadata, the dnf metadata and every RPM in the repositories are signed with one OpenPGP key, published at `https://packages.kividb.io/kividb.asc` (and, for apt, `kividb.gpg`). Its fingerprint is:

**`6492 17DE 0F7F D7DB 3D7B  AC3A E21D 8F6E DDE5 F489`** (`KiviDB Packages <packages@kividb.io>`, RSA 4096, created 12 November 2026)

It is also published in the [KiviDB repository's SECURITY.md](https://github.com/kividbio/kividb/blob/master/SECURITY.md#package-signing-key), which the site that serves the key does not control. To see the fingerprint of the key you downloaded:

```bash
curl -fsSL https://packages.kividb.io/kividb.asc | gpg --show-keys
```

If it is not the fingerprint above, do not install from the repository.

## Docker

Images are on the GitHub Container Registry and Docker Hub (`kividb/kividb`), with the same tags in both:

```bash
docker run -d -p 6380:6380 ghcr.io/kividbio/kividb:v1.2.1
# or
docker run -d -p 6380:6380 kividb/kividb:v1.2.1
```

| Tag | Build |
|---|---|
| `v1.2.1`, `1.2`, `latest` | default |
| `v1.2.1-lua` | with Lua scripting |
| `v1.2.1-tls` | with TLS |
| `v1.2.1-full` | Lua and TLS |

Images are built for `amd64` and `arm64`. `1.2` and `latest` move to each new release; pin a version tag in production. The `v1.2.0` tags stay published.

**Arguments replace the image's default command.** A container is always reached through its network, never over loopback, so the image runs with `--protected-mode no` by default. Any arguments you pass replace that, and protected mode is on again. When you pass your own flags, set a password, or add `--protected-mode no` yourself:

```bash
docker run -d -p 6380:6380 ghcr.io/kividbio/kividb:v1.2.1 --requirepass "change-me"
```

**Keeping data.** Mount a volume on `/home/kividb`, where the server runs as UID 1000. With `--aof`, every write is also appended to a log that is replayed on start:

```bash
docker run -d -p 6380:6380 -v "$(pwd)/data:/home/kividb" \
  ghcr.io/kividbio/kividb:v1.2.1 --aof --requirepass "change-me"
```

Give each server a volume of its own: a second server started on a data directory another one is using waits until the first has stopped. See [Persistence](../guides/persistence.md#one-server-per-data-directory).

**`CONFIG REWRITE`** needs a configuration file to rewrite. The image starts the server without one, so since 1.2.1 `CONFIG REWRITE` there answers `ERR The server is running without a config file`. To use it, mount a file and start the server with `--configfile` pointing at it.

The image has no shell, no `redis-cli`, and, since 1.2, no OpenSSL either (TLS is built into the binary). Connect from another container, for example:

```bash
docker run --rm -it --network container:<name> redis redis-cli -p 6380
```

**io_uring.** On Linux, KiviDB uses io_uring when the kernel allows it, and Tokio otherwise. Docker's default seccomp profile blocks io_uring, so in a container KiviDB uses Tokio unless you run it with `--security-opt seccomp=unconfined`. Understand what that allows before you use it in production.

## Release binaries

Binaries for Linux (x86_64, aarch64) and macOS (Apple silicon, Intel) are attached to each [GitHub release](https://github.com/kividbio/kividb/releases):

```bash
curl -LO https://github.com/kividbio/kividb/releases/download/v1.2.1/kividb-linux-x86_64.tar.gz
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

The Linux binaries need glibc 2.34 or newer, and the aarch64 one an ARMv8.1 CPU or newer: AWS Graviton2 and later, or Ampere. It does not run on a Raspberry Pi 4.

## Homebrew

On macOS only, the default build installs with:

```bash
brew install kividbio/tap/kividb
kividb --version
```

On Linux, use the [package repositories](#linux-package-repositories) instead.

## Cargo

From 1.2.1, each release is published on crates.io as the crate `kividb`:

```bash
cargo install --locked kividb                      # the default build
cargo install --locked kividb --features lua,tls   # full; or lua, or tls
cargo binstall kividb                              # the release's own binary
```

KiviDB runs on Linux and macOS only.

- `cargo install` builds the server from source, with a stable Rust toolchain, 1.89 or newer. `--locked` builds it with the dependency versions the release was built and tested with. The build takes several minutes. Since it compiles on the machine itself, it also works with a glibc older than 2.34.
- [`cargo binstall`](https://github.com/cargo-bins/cargo-binstall) downloads the release's binary of the default build, for Linux (x86_64, aarch64) and macOS (Intel, Apple silicon), and compiles only on other targets. The Linux binaries have the needs given under [Release binaries](#release-binaries).

## Linux packages

Each GitHub release also has `.deb` and `.rpm` packages of the default build, for `amd64` and `arm64`. They are the packages in the [repositories](#linux-package-repositories), which add a signature to the RPMs, and install the same files:

```bash
curl -LO https://github.com/kividbio/kividb/releases/download/v1.2.1/kividb_amd64.deb
sudo apt install ./kividb_amd64.deb
# or
curl -LO https://github.com/kividbio/kividb/releases/download/v1.2.1/kividb.x86_64.rpm
sudo dnf install ./kividb.x86_64.rpm
```

The `arm64` files are `kividb_arm64.deb` and `kividb.aarch64.rpm`. A package installed this way is not upgraded by `apt upgrade` or `dnf upgrade` unless the repository is set up too.

To upgrade servers that replicate, upgrade the replicas first and their master last. See [Upgrading](upgrading.md).

## Checking what you downloaded

`SHA256SUMS.txt` shows that a file arrived whole. Since 1.2, every file and image also carries a signed build attestation, which shows that it was built by KiviDB's release workflow from the tagged commit. Check one with the GitHub CLI:

```bash
gh attestation verify kividb-linux-x86_64.tar.gz --repo kividbio/kividb
gh attestation verify oci://ghcr.io/kividbio/kividb:v1.2.1 --repo kividbio/kividb
```

The packages in the repositories are checked by the package manager, against the [signing key](#the-signing-key). The RPMs there carry that key's signature, so their checksums differ from the release's files.

## From source

You need a stable Rust toolchain, 1.89 or newer:

```bash
git clone https://github.com/kividbio/kividb.git
cd kividb
git checkout v1.2.1

cargo build --release                      # default build
cargo build --release --features lua       # with Lua scripting
cargo build --release --features tls       # with TLS
cargo build --release --features lua,tls   # both

./target/release/kividb
```

Each release also has a source tag without the `v`, such as `1.2.1-src`, for ports and packages that fetch GitHub's source archive by tag. It builds the same server.

`docker build -t kividb .` builds the default image. `docker build --build-arg KIVIDB_FEATURES=lua,tls -t kividb:full .` builds another build.

## Next

[Quick start](quick-start.md): connect and store some data.
