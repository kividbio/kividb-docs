"""Find which subcommands a KiviDB release has, by asking it.

usage: python -I tools/probe.py <version> <out dir> <binary> [<lua binary>]

A release's `COMMAND` does not always list subcommands (1.1 does not), and
`COMMANDS.md` has no row for some (`ACL SETUSER`). So each container is sent
each subcommand Redis 8 has, and KiviDB's own, with three placeholder
arguments, on a throwaway server: a subcommand exists unless the reply says it
is unknown. `CLUSTER` is asked on a server in cluster mode, which is the only
one that answers its subcommands; `FUNCTION` and `SCRIPT` on the Lua build, if
one is given. Writes `<out dir>/<version>/probed.json`: container -> the
subcommands found, and those that could not be told (`unsure`).
"""

import json
import os
import socket
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import extract  # noqa: E402

# Redis 8's subcommands, KiviDB's own (BACKUP, HOTKEYS), and RediSearch's.
CANDIDATES = {
    "ACL": "CAT DELUSER DRYRUN GENPASS GETUSER HELP LIST LOAD LOG SAVE SETUSER USERS WHOAMI",
    "BACKUP": "ABORT CLEANUP HELP LIST SEAL START STATUS",
    "CLIENT": "CACHING GETNAME GETREDIR HELP ID INFO KILL LIST NO-EVICT NO-TOUCH PAUSE REPLY "
              "SETINFO SETNAME TRACKING TRACKINGINFO UNBLOCK UNPAUSE",
    "CLUSTER": "ADDSLOTS ADDSLOTSRANGE BUMPEPOCH COUNT-FAILURE-REPORTS COUNTKEYSINSLOT DELSLOTS "
               "DELSLOTSRANGE FLUSHSLOTS FORGET GETKEYSINSLOT HELP INFO KEYSLOT LINKS MEET "
               "MIGRATION MYID MYSHARDID NODES REPLICAS REPLICATE SAVECONFIG SET-CONFIG-EPOCH "
               "SETSLOT SHARDS SLAVES SLOT-STATS SLOTS",
    "COMMAND": "COUNT DOCS GETKEYS GETKEYSANDFLAGS HELP INFO LIST",
    "CONFIG": "GET HELP RESETSTAT REWRITE SET",
    "FUNCTION": "DELETE DUMP FLUSH HELP KILL LIST LOAD RESTORE STATS",
    "HOTKEYS": "GET HELP RESET START STOP",
    "LATENCY": "DOCTOR GRAPH HELP HISTOGRAM HISTORY LATEST RESET",
    "MEMORY": "DOCTOR HELP MALLOC-STATS PURGE STATS USAGE",
    "MODULE": "HELP LIST LOAD LOADEX UNLOAD",
    "OBJECT": "ENCODING FREQ HELP IDLETIME REFCOUNT",
    "PUBSUB": "CHANNELS HELP NUMPAT NUMSUB SHARDCHANNELS SHARDNUMSUB",
    "SCRIPT": "DEBUG EXISTS FLUSH HELP KILL LOAD",
    "SLOWLOG": "GET HELP LEN RESET",
    "XGROUP": "CREATE CREATECONSUMER DELCONSUMER DESTROY HELP SETID",
    "XINFO": "CONSUMERS GROUPS HELP STREAM",
    "FT.CONFIG": "GET HELP SET",
    "FT.CURSOR": "DEL READ",
    "JSON.DEBUG": "HELP MEMORY",
    "PFDEBUG": "DECODE ENCODING GETREG RESET TODENSE",
}
# Not probed: they would stop or reshape the throwaway server.
NEVER = {("CLUSTER", "FAILOVER"), ("CLUSTER", "RESET")}
PLACEHOLDERS = ["__probe__", "__probe__", "__probe__"]


def start(binary, *extra):
    port = extract.free_port()
    work = tempfile.mkdtemp(prefix="kividb-probe-")
    server = subprocess.Popen(
        [binary, "--port", str(port), "--bind", "127.0.0.1", "--dir", work,
         "--configfile", os.path.join(work, "none.conf"), "--loglevel", "warning", *extra],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    extract.Conn(port)
    return server, port


def ask(port, container, sub, nargs):
    """The reply to `container sub` with `nargs` placeholders, or None."""
    try:
        c = extract.Conn(port)
        c.sock.settimeout(3)
        reply = c.cmd(*container.split(), sub, *PLACEHOLDERS[:nargs])
        c.sock.close()
        return reply
    except (socket.timeout, ConnectionError, OSError):
        return None


def probe(port, container, sub):
    """True if `container sub` exists, False if unknown, None if it cannot be told.

    Tried with 0, 1 and 3 placeholders: an error that says "unknown
    subcommand or wrong number of arguments", as Redis's do, may only mean
    the count was wrong, so it decides nothing; a reply of any other kind
    means the subcommand exists."""
    unsure = False
    for nargs in (0, 1, 3):
        reply = ask(port, container, sub, nargs)
        if reply is None:
            unsure = True
            continue
        if not isinstance(reply, dict):
            return True
        error = reply.get("error", "").lower()
        if "cluster support disabled" in error or "not supported by kividb (requires lua)" in error:
            return None
        if "wrong number of arguments" in error and "unknown subcommand or" in error:
            continue
        if "unknown subcommand" in error or "unknown command" in error:
            continue
        return True
    return None if unsure else False


def run(binary, containers, *extra):
    found, unsure = {}, {}
    server, port = start(binary, *extra)
    try:
        for container in containers:
            for sub in CANDIDATES[container].split():
                if (container, sub) in NEVER:
                    continue
                result = probe(port, container, sub)
                if result is None:
                    unsure.setdefault(container, []).append(sub)
                elif result:
                    found.setdefault(container, []).append(sub)
    finally:
        server.terminate()
        server.wait(timeout=30)
    return found, unsure


def main():
    version, out, binary = sys.argv[1:4]
    lua = sys.argv[4] if len(sys.argv) > 4 else None
    plain = [c for c in CANDIDATES if c not in ("CLUSTER", "FUNCTION", "SCRIPT")]
    found, unsure = run(binary, plain)
    f, u = run(binary, ["CLUSTER"], "--cluster-enabled", "yes")
    found.update(f)
    unsure.update(u)
    f, u = run(lua or binary, ["FUNCTION", "SCRIPT"])
    found.update(f)
    unsure.update(u)
    dest = Path(out) / version
    dest.mkdir(parents=True, exist_ok=True)
    result = {"found": dict(sorted(found.items())), "unsure": dict(sorted(unsure.items())),
              "lua": bool(lua)}
    (dest / "probed.json").write_text(json.dumps(result, indent=1, sort_keys=True) + "\n",
                                      encoding="utf-8", newline="\n")
    print(json.dumps({k: len(v) for k, v in found.items()}), "unsure:", unsure)


if __name__ == "__main__":
    main()
