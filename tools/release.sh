#!/usr/bin/env bash
# Extract one KiviDB release's data and regenerate the pages, in one go.
#
# usage: tools/release.sh <release> <kividb source dir>
#
#   <release>      the release's name in versions.json, e.g. 1.2.0
#   <source dir>   a checkout of kividb at that release's tag or commit
#
# Builds the default and the `lua` builds of the source, each in a target
# directory of its own (two releases can share a Cargo version, and a shared
# target directory then reuses the other's binary), and runs, in order:
# probe.py, extract.py, probe_config.py, diff.py, generate.py. Writes
# data/<release>/, data/history.json and the generated parts of content/.
#
# Run it on Linux, with Rust and Python 3, from anywhere. TARGET_ROOT sets
# where the builds go (default: ~/kividb-docs-target). SKIP_BUILD=1 uses
# binaries already built there.
set -euo pipefail

release=${1:?usage: tools/release.sh <release> <kividb source dir>}
source=$(cd "${2:?usage: tools/release.sh <release> <kividb source dir>}" && pwd)
docs=$(cd "$(dirname "$0")/.." && pwd)
target=${TARGET_ROOT:-$HOME/kividb-docs-target}

build() {
    local name=$1; shift
    if [ -z "${SKIP_BUILD:-}" ]; then
        (cd "$source" && CARGO_TARGET_DIR="$target/$release-$name" cargo build --release "$@")
    fi
    echo "$target/$release-$name/release/kividb"
}

default_bin=$(build default | tail -1)
lua_bin=$(build lua --features lua | tail -1)
"$default_bin" --version
"$lua_bin" --version

cd "$docs"
python3 -I tools/probe.py "$release" data "$default_bin" "$lua_bin"
python3 -I tools/extract.py "$default_bin" "$release" "$source" data
python3 -I tools/probe_config.py "$default_bin" "$release" data
python3 -I tools/diff.py data
python3 -I tools/generate.py
git -C "$docs" status --short | head -50
