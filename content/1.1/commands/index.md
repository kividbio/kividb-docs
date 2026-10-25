---
title: "Commands"
description: "Every command of KiviDB 1.1."
version: "1.1"
weight: 10
---

Every command KiviDB 1.1 has, by group. A command's page gives its syntax, what it does, and what changed in it since 1.1.0.

## Acl

| Command | Summary | Since |
|---|---|---|
| [`ACL`](acl.md) | ACL and its subcommands. | 1.1.0 |
| [`AUTH`](auth.md) | Authenticate the connection; AUTH password (legacy) or AUTH username password (Redis 6 ACL form); required when --requirepass is set or when the user has a password; PING, AUTH, QUIT, HELLO, and RESE… | 1.1.0 |

## Array

| Command | Summary | Since |
|---|---|---|
| [`ARCOUNT`](arcount.md) | Number of non-empty elements, or 0 | 1.1.0 |
| [`ARDEL`](ardel.md) | Delete elements at the given indices; returns the number actually removed | 1.1.0 |
| [`ARDELRANGE`](ardelrange.md) | Delete elements in one or more inclusive ranges; overlapping ranges count each element once | 1.1.0 |
| [`ARGET`](arget.md) | Get the value at an index, or nil | 1.1.0 |
| [`ARGETRANGE`](argetrange.md) | Get every slot in the range including nils for empty ones; start > end returns the range in reverse. | 1.1.0 |
| [`ARGREP`](argrep.md) | Search elements by textual predicate. | 1.1.0 |
| [`ARINFO`](arinfo.md) | Array metadata: count, len, next-insert-index, slices, directory-size, super-dir-entries, slice-size (plus ring-size for rings). | 1.1.0 |
| [`ARINSERT`](arinsert.md) | Insert at the cursor, advancing it once per value; returns the last index written | 1.1.0 |
| [`ARLASTITEMS`](arlastitems.md) | The most recently inserted elements, oldest-first by default, newest-first with REV. | 1.1.0 |
| [`ARLEN`](arlen.md) | Highest occupied index + 1, or 0 | 1.1.0 |
| [`ARMGET`](armget.md) | Get values at multiple indices; order is preserved and empty slots return nil | 1.1.0 |
| [`ARMSET`](armset.md) | Set multiple index-value pairs, non-contiguous and in any order; returns the number of previously-empty slots filled | 1.1.0 |
| [`ARNEXT`](arnext.md) | The index the next ARINSERT would use; 0 for a missing key, nil when the cursor is exhausted | 1.1.0 |
| [`AROP`](arop.md) | Aggregate over non-empty elements in a range. | 1.1.0 |
| [`ARRING`](arring.md) | Insert into a ring buffer of size, wrapping at size so newer values overwrite older ones; shrinking size truncates. | 1.1.0 |
| [`ARSCAN`](arscan.md) | Iterate existing elements in a range, skipping empty slots. | 1.1.0 |
| [`ARSEEK`](arseek.md) | Move the insert cursor; returns 1 if set, 0 if the key does not exist. | 1.1.0 |
| [`ARSET`](arset.md) | Set one or more contiguous values starting at index; returns the number of previously-empty slots filled | 1.1.0 |

## Bitmap

| Command | Summary | Since |
|---|---|---|
| [`BITCOUNT`](bitcount.md) | Count the number of set bits; without range counts the whole string; BYTE mode (default) treats start/end as byte indices; BIT mode treats them as bit indices; negative indices count from the end | 1.1.0 |
| [`BITFIELD`](bitfield.md) | Perform arbitrary bitfield integer operations in a single call; encoding is u<n> for unsigned or i<n> for signed where n is the bit width (1–63 for unsigned, 1–64 for signed); SET returns the old val… | 1.1.0 |
| [`BITFIELD_RO`](bitfield_ro.md) | Read-only variant of BITFIELD; only GET subcommands are accepted | 1.1.0 |
| [`BITOP`](bitop.md) | Perform a bitwise operation across one or more source keys and store the result at destkey; shorter strings are zero-padded; NOT requires exactly one source key; returns the length of the destination… | 1.1.0 |
| [`BITPOS`](bitpos.md) | Find the position of the first set (1) or clear (0) bit; returns -1 if not found; for clear-bit search with no explicit end, returns the first bit past the string | 1.1.0 |
| [`GETBIT`](getbit.md) | Return the bit value (0 or 1) at offset; returns 0 if key missing or offset beyond string length | 1.1.0 |
| [`SETBIT`](setbit.md) | Set or clear the bit at offset; auto-extends the string with zero bytes if needed; returns the old bit value; AOF-logged | 1.1.0 |

## Cluster

| Command | Summary | Since |
|---|---|---|
| [`ASKING`](asking.md) | Per-connection single-shot flag. | 1.1.0 |
| [`CLUSTER`](cluster.md) | List replicas of a given master. | 1.1.0 |
| [`MIGRATE`](migrate.md) | Serialise each key, RESTORE it on the destination with its TTL, and delete it here once the destination has acknowledged. | 1.1.0 |
| [`READONLY`](readonly.md) | Per-connection flag: read commands for slots this node replicates are served here instead of redirected to the master. | 1.1.0 |
| [`READWRITE`](readwrite.md) | Clears the READONLY flag. | 1.1.0 |

## Generic

| Command | Summary | Since |
|---|---|---|
| [`COPY`](copy.md) | Copies the value at source to destination, with its expiry. | 1.1.0 |
| [`DEL`](del.md) | Deletes the given keys, of any type. | 1.1.0 |
| [`DUMP`](dump.md) | Serializes the value at key into a payload that RESTORE turns back into the value. | 1.1.0 |
| [`EXISTS`](exists.md) | Counts how many of the given keys exist. | 1.1.0 |
| [`EXPIRE`](expire.md) | Makes key expire after seconds. | 1.1.0 |
| [`EXPIREAT`](expireat.md) | Makes key expire at a Unix time, in seconds. | 1.1.0 |
| [`EXPIRETIME`](expiretime.md) | Returns the Unix time, in seconds, at which key expires. | 1.1.0 |
| [`KEYS`](keys.md) | Returns every key of the current database that matches a glob-style pattern. | 1.1.0 |
| [`MOVE`](move.md) | Moves key to database db. | 1.1.0 |
| [`OBJECT`](object.md) | Inspects how a key's value is stored and used. | 1.1.0 |
| [`PERSIST`](persist.md) | Removes the expiry of key, so that it is kept until deleted. | 1.1.0 |
| [`PEXPIRE`](pexpire.md) | Makes key expire after milliseconds. | 1.1.0 |
| [`PEXPIREAT`](pexpireat.md) | Makes key expire at a Unix time, in milliseconds. | 1.1.0 |
| [`PEXPIRETIME`](pexpiretime.md) | Returns the Unix time, in milliseconds, at which key expires. | 1.1.0 |
| [`PTTL`](pttl.md) | Returns how long key has before it expires, in milliseconds. | 1.1.0 |
| [`RANDOMKEY`](randomkey.md) | Returns a key of the current database, picked at random. | 1.1.0 |
| [`RENAME`](rename.md) | Renames source to destination, with its expiry. | 1.1.0 |
| [`RENAMENX`](renamenx.md) | Renames source to destination only if destination does not exist. | 1.1.0 |
| [`RESTORE`](restore.md) | Creates key from a DUMP payload. | 1.1.0 |
| [`SCAN`](scan.md) | Goes through the keys of the current database a page at a time. | 1.1.0 |
| [`SORT`](sort.md) | Sorts the elements of a list, set or sorted set, as numbers unless ALPHA is given. | 1.1.0 |
| [`SORT_RO`](sort_ro.md) | SORT without STORE: it only reads, so it can be sent to a read-only replica. | 1.1.0 |
| [`SWAPDB`](swapdb.md) | Swaps the contents of two databases in one step, keys and expiries together. | 1.1.0 |
| [`TOUCH`](touch.md) | Counts how many of the given keys exist. | 1.1.0 |
| [`TTL`](ttl.md) | Returns how long key has before it expires, in seconds. | 1.1.0 |
| [`TYPE`](type.md) | Returns the type of the value at key. | 1.1.0 |
| [`UNLINK`](unlink.md) | Deletes the given keys, like DEL, but frees large values in the background. | 1.1.0 |

## Geospatial

| Command | Summary | Since |
|---|---|---|
| [`GEOADD`](geoadd.md) | Add one or more members to a geospatial index; NX only adds new members (never updates existing); XX only updates existing members (never adds new); CH changes the return value from count-of-added to… | 1.1.0 |
| [`GEODIST`](geodist.md) | Return the distance between two members; default unit is metres (M); returns nil if either member is missing | 1.1.0 |
| [`GEOHASH`](geohash.md) | Return the standard 11-character base32 geohash string for each member; nil for missing members | 1.1.0 |
| [`GEOPOS`](geopos.md) | Return [longitude, latitude] pairs for each member; nil for missing members | 1.1.0 |
| [`GEORADIUS`](georadius.md) | Query members within a radius of explicit coordinates; STORE writes results to a destination key as a geo index; STOREDIST writes with distance scores; AOF-logged when STORE or STOREDIST is used | 1.1.0 |
| [`GEORADIUSBYMEMBER`](georadiusbymember.md) | Query members within a radius of an existing member; supports STORE and STOREDIST; AOF-logged when storing | 1.1.0 |
| [`GEORADIUSBYMEMBER_RO`](georadiusbymember_ro.md) | Read-only variant of GEORADIUSBYMEMBER; does not support STORE or STOREDIST | 1.1.0 |
| [`GEORADIUS_RO`](georadius_ro.md) | Read-only variant of GEORADIUS; does not support STORE or STOREDIST | 1.1.0 |
| [`GEOSEARCH`](geosearch.md) | Query members inside a circle or axis-aligned box; FROMMEMBER uses an existing member as the centre; FROMLONLAT uses explicit coordinates; BYRADIUS filters by great-circle distance; BYBOX filters by… | 1.1.0 |
| [`GEOSEARCHSTORE`](geosearchstore.md) | Same search as GEOSEARCH but writes the results into destination as a sorted set; without STOREDIST the score is the geohash (so the destination is itself a valid geo index); with STOREDIST the score… | 1.1.0 |

## Hash

| Command | Summary | Since |
|---|---|---|
| [`HDEL`](hdel.md) | Deletes fields from the hash at key. | 1.1.0 |
| [`HEXISTS`](hexists.md) | Tells whether field exists in the hash at key. | 1.1.0 |
| [`HEXPIRE`](hexpire.md) | Makes fields of the hash at key expire after seconds. | 1.1.0 |
| [`HEXPIREAT`](hexpireat.md) | Makes fields of the hash at key expire at a Unix time, in seconds. | 1.1.0 |
| [`HEXPIRETIME`](hexpiretime.md) | Returns the Unix time, in seconds, at which fields of the hash at key expire. | 1.1.0 |
| [`HGET`](hget.md) | Returns the value of field in the hash at key. | 1.1.0 |
| [`HGETALL`](hgetall.md) | Returns every field of the hash at key with its value. | 1.1.0 |
| [`HGETDEL`](hgetdel.md) | Returns the values of fields of the hash at key and deletes those fields, in one step. | 1.1.0 |
| [`HGETEX`](hgetex.md) | Returns the values of fields of the hash at key and, optionally, changes their expiry, in one step. | 1.1.0 |
| [`HIMPORT`](himport.md) | Loads many hashes that have the same fields, without sending the field names for each: a command of Redis 8.10. | 1.1.0 |
| [`HINCRBY`](hincrby.md) | Adds increment, a 64-bit integer, to the integer value of field in the hash at key. | 1.1.0 |
| [`HINCRBYFLOAT`](hincrbyfloat.md) | Adds increment, a floating-point number, to the value of field in the hash at key. | 1.1.0 |
| [`HKEYS`](hkeys.md) | Returns the field names of the hash at key. | 1.1.0 |
| [`HLEN`](hlen.md) | Returns the number of fields in the hash at key. | 1.1.0 |
| [`HMGET`](hmget.md) | Returns the values of several fields of the hash at key. | 1.1.0 |
| [`HMSET`](hmset.md) | Another name for HSET, kept for old clients. | 1.1.0 |
| [`HPERSIST`](hpersist.md) | Removes the expiry of fields of the hash at key. | 1.1.0 |
| [`HPEXPIRE`](hpexpire.md) | HEXPIRE with the time in milliseconds. | 1.1.0 |
| [`HPEXPIREAT`](hpexpireat.md) | HEXPIREAT with the time in milliseconds. | 1.1.0 |
| [`HPEXPIRETIME`](hpexpiretime.md) | HEXPIRETIME in milliseconds. | 1.1.0 |
| [`HPTTL`](hpttl.md) | HTTL in milliseconds. | 1.1.0 |
| [`HRANDFIELD`](hrandfield.md) | Returns fields of the hash at key, picked at random. | 1.1.0 |
| [`HSCAN`](hscan.md) | Goes through the fields of the hash at key a page at a time, as SCAN goes through keys. | 1.1.0 |
| [`HSET`](hset.md) | Sets fields of the hash at key, each to its value. | 1.1.0 |
| [`HSETEX`](hsetex.md) | Sets fields of the hash at key, with one expiry for all of them, in one step. | 1.1.0 |
| [`HSETNX`](hsetnx.md) | Sets field in the hash at key only if the field does not exist. | 1.1.0 |
| [`HSTRLEN`](hstrlen.md) | Returns the length, in bytes, of the value of field in the hash at key. | 1.1.0 |
| [`HTTL`](httl.md) | Returns how long fields of the hash at key have before they expire, in seconds. | 1.1.0 |
| [`HVALS`](hvals.md) | Returns the values of the hash at key. | 1.1.0 |

## Hyperloglog

| Command | Summary | Since |
|---|---|---|
| [`PFADD`](pfadd.md) | Add one or more elements to the HyperLogLog; creates the key if it does not exist; returns 1 if the internal representation was modified (cardinality estimate changed), 0 otherwise; calling with no e… | 1.1.0 |
| [`PFCOUNT`](pfcount.md) | Return the approximated cardinality of the set observed by the HyperLogLog at key; with multiple keys, returns the cardinality of the union by merging into a temporary HyperLogLog without persisting… | 1.1.0 |
| [`PFDEBUG`](pfdebug.md) | PFDEBUG and its subcommands. | 1.1.0 |
| [`PFMERGE`](pfmerge.md) | Merge one or more source HyperLogLogs into destkey by taking the element-wise maximum of all registers; missing source keys are treated as empty; AOF-logged | 1.1.0 |
| [`PFSELFTEST`](pfselftest.md) | Run internal correctness tests of the HyperLogLog implementation: verifies empty cardinality returns 0, estimation accuracy is within 2% for 10,000 elements, and register encode/decode round-trips co… | 1.1.0 |

## Json

| Command | Summary | Since |
|---|---|---|
| [`JSON.ARRAPPEND`](json.arrappend.md) | Append to each matched array; returns the new lengths | 1.1.0 |
| [`JSON.ARRINDEX`](json.arrindex.md) | The index of the first element equal to value in each matched array, or -1; stop is exclusive and 0 means the end | 1.1.0 |
| [`JSON.ARRINSERT`](json.arrinsert.md) | Insert before index in each matched array; returns the new lengths | 1.1.0 |
| [`JSON.ARRLEN`](json.arrlen.md) | The length of each matched array | 1.1.0 |
| [`JSON.ARRPOP`](json.arrpop.md) | Remove and return an element (default -1, the last) from each matched array; an index out of range means the nearest end | 1.1.0 |
| [`JSON.ARRTRIM`](json.arrtrim.md) | Keep the inclusive range in each matched array; returns the new lengths | 1.1.0 |
| [`JSON.CLEAR`](json.clear.md) | Empty each matched array and object and set each matched number to 0; returns how many values changed | 1.1.0 |
| [`JSON.DEBUG`](json.debug.md) | JSON.DEBUG and its subcommands. | 1.1.0 |
| [`JSON.DEL`](json.del.md) | Delete every value the path matches; returns how many. | 1.1.0 |
| [`JSON.FORGET`](json.forget.md) | Alias for JSON.DEL | 1.1.0 |
| [`JSON.GET`](json.get.md) | No path: the whole document. | 1.1.0 |
| [`JSON.MERGE`](json.merge.md) | RFC 7396 merge patch at each match — members are merged, a null deletes, anything else replaces | 1.1.0 |
| [`JSON.MGET`](json.mget.md) | The path evaluated against each key, as JSON text; nil for a missing key or one of another type | 1.1.0 |
| [`JSON.MSET`](json.mset.md) | JSON.SET for several key-path-value triples; every argument is checked before any key is touched | 1.1.0 |
| [`JSON.NUMINCRBY`](json.numincrby.md) | Add to each matched number. | 1.1.0 |
| [`JSON.NUMMULTBY`](json.nummultby.md) | The same, multiplying | 1.1.0 |
| [`JSON.OBJKEYS`](json.objkeys.md) | The member names of each matched object, in the order they were added | 1.1.0 |
| [`JSON.OBJLEN`](json.objlen.md) | The number of members of each matched object | 1.1.0 |
| [`JSON.RESP`](json.resp.md) | Each match in RESP: null as nil, booleans as true/false, integers as integers, other numbers and strings as bulk strings, an array as [ followed by its elements, an object as { followed by alternatin… | 1.1.0 |
| [`JSON.SET`](json.set.md) | Set every value the path matches; if it matches nothing and ends in a member name under a single existing object, add that member. | 1.1.0 |
| [`JSON.STRAPPEND`](json.strappend.md) | Append a JSON string to each matched string; returns the new lengths | 1.1.0 |
| [`JSON.STRLEN`](json.strlen.md) | The length of each matched string; nil for other types | 1.1.0 |
| [`JSON.TOGGLE`](json.toggle.md) | Flip each matched boolean; returns the new values as 1 and 0 (a legacy path: "true" or "false") | 1.1.0 |
| [`JSON.TYPE`](json.type.md) | The type of each match: object, array, string, integer, number, boolean, null | 1.1.0 |

## List

| Command | Summary | Since |
|---|---|---|
| [`BLMOVE`](blmove.md) | LMOVE that waits, as BLPOP does, until source has an element or timeout seconds have passed. | 1.1.0 |
| [`BLMOVEM`](blmovem.md) | LMOVEM that waits until source has an element, or, with EXACTLY, enough of them, or until timeout seconds have passed. | 1.1.0 |
| [`BLMPOP`](blmpop.md) | LMPOP that waits until one of the lists has an element, or timeout seconds have passed. | 1.1.0 |
| [`BLPOP`](blpop.md) | Pops the first element of the first non-empty list of those given. | 1.1.0 |
| [`BRPOP`](brpop.md) | Like BLPOP, but pops the last element. | 1.1.0 |
| [`BRPOPLPUSH`](brpoplpush.md) | RPOPLPUSH that waits until source has an element or timeout seconds have passed. | 1.1.0 |
| [`LINDEX`](lindex.md) | Returns the element at index in the list at key. | 1.1.0 |
| [`LINSERT`](linsert.md) | Inserts element before or after the first element equal to pivot, in the list at key. | 1.1.0 |
| [`LLEN`](llen.md) | Returns the number of elements in the list at key. | 1.1.0 |
| [`LMOVE`](lmove.md) | Removes an element from one end of source and adds it to one end of destination, in one step. | 1.1.0 |
| [`LMOVEM`](lmovem.md) | Moves several elements from one end of source to one end of destination in one step, a command of Redis 8.10. | 1.1.0 |
| [`LMPOP`](lmpop.md) | Pops elements from the first of the given lists that is not empty. | 1.1.0 |
| [`LPOP`](lpop.md) | Removes and returns the first element of the list at key. | 1.1.0 |
| [`LPOS`](lpos.md) | Returns the index of an element equal to element in the list at key. | 1.1.0 |
| [`LPUSH`](lpush.md) | Adds values to the head (left) of the list at key, one after another, so the last value given ends up first. | 1.1.0 |
| [`LPUSHX`](lpushx.md) | Adds values to the head of the list at key, only if the list exists. | 1.1.0 |
| [`LRANGE`](lrange.md) | Returns the elements of the list at key from index start to index stop, both included. | 1.1.0 |
| [`LREM`](lrem.md) | Removes elements equal to element from the list at key:
- count greater than 0: the first count of them, from the head;
- count less than 0: the last -count of them, from the tail;
- count 0: all of… | 1.1.0 |
| [`LSET`](lset.md) | Replaces the element at index in the list at key. | 1.1.0 |
| [`LTRIM`](ltrim.md) | Keeps only the elements from index start to index stop, both included, and removes the rest. | 1.1.0 |
| [`RPOP`](rpop.md) | Removes and returns the last element of the list at key. | 1.1.0 |
| [`RPOPLPUSH`](rpoplpush.md) | Removes the last element of source and adds it to the head of destination. | 1.1.0 |
| [`RPUSH`](rpush.md) | Adds values to the tail (right) of the list at key, in the order given. | 1.1.0 |
| [`RPUSHX`](rpushx.md) | Adds values to the tail of the list at key, only if the list exists. | 1.1.0 |

## Observability

| Command | Summary | Since |
|---|---|---|
| [`HOTKEYS`](hotkeys.md) | HOTKEYS and its subcommands. | 1.1.0 |
| [`LATENCY`](latency.md) | LATENCY and its subcommands. | 1.1.0 |
| [`SLOWLOG`](slowlog.md) | SLOWLOG and its subcommands. | 1.1.0 |

## Other

| Command | Summary | Since |
|---|---|---|
| [`BACKUP`](backup.md) | The BACKUP command. | 1.1.0 |
| [`FAILOVER`](failover.md) | The FAILOVER command. | 1.1.0 |
| [`GEODELBYMEMBER`](geodelbymember.md) | The GEODELBYMEMBER command. | 1.1.0 |
| [`MODULE`](module.md) | The MODULE command. | 1.1.0 |
| [`XIDMPRECORD`](xidmprecord.md) | The XIDMPRECORD command. | 1.1.1 |

## Pub sub

| Command | Summary | Since |
|---|---|---|
| [`PING`](ping.md) | In subscriber mode returns ["pong", message] (a 2-element array), not +PONG. | 1.1.0 |
| [`PSUBSCRIBE`](psubscribe.md) | Subscribe to all channels matching a glob pattern. | 1.1.0 |
| [`PUBLISH`](publish.md) | Post a message to a channel. | 1.1.0 |
| [`PUBSUB`](pubsub.md) | PUBSUB and its subcommands. | 1.1.0 |
| [`PUNSUBSCRIBE`](punsubscribe.md) | Unsubscribe from patterns. | 1.1.0 |
| [`QUIT`](quit.md) | Close the connection cleanly | 1.1.0 |
| [`RESET`](reset.md) | Unsubscribe from everything and put the connection back as it was when it was opened: no transaction or watches, database 0, RESP2, no name, no tracking, and the default user if that needs no password | 1.1.0 |
| [`SPUBLISH`](spublish.md) | Post a message to a shard channel. | 1.1.0 |
| [`SSUBSCRIBE`](ssubscribe.md) | Subscribe to one or more shard channels. | 1.1.0 |
| [`SUBSCRIBE`](subscribe.md) | Subscribe to one or more channels. | 1.1.0 |
| [`SUNSUBSCRIBE`](sunsubscribe.md) | Unsubscribe from shard channels. | 1.1.0 |
| [`UNSUBSCRIBE`](unsubscribe.md) | Unsubscribe from channels. | 1.1.0 |

## Scripting

| Command | Summary | Since |
|---|---|---|
| [`EVAL`](eval.md) | Execute a Lua script | 1.1.0 |
| [`EVALSHA`](evalsha.md) | Execute a script already in the cache by SHA1 | 1.1.0 |
| [`EVALSHA_RO`](evalsha_ro.md) | Read-only EVALSHA | 1.1.0 |
| [`EVAL_RO`](eval_ro.md) | Read-only script; mutating commands fail | 1.1.0 |
| [`FCALL`](fcall.md) | Call a registered library function. | 1.1.0 |
| [`FCALL_RO`](fcall_ro.md) | Read-only FCALL: refused for a function not registered with the no-writes flag | 1.1.0 |
| [`FUNCTION`](function.md) | Serialise every library, and load such a payload. | 1.1.0 |
| [`SCRIPT`](script.md) | SCRIPT and its subcommands. | 1.1.0 |

## Server

| Command | Summary | Since |
|---|---|---|
| [`BGREWRITEAOF`](bgrewriteaof.md) | Trigger a background AOF rewrite; returns ERR if AOF is not enabled | 1.1.0 |
| [`BGSAVE`](bgsave.md) | Save a snapshot in the background | 1.1.0 |
| [`CLIENT`](client.md) | CLIENT and its subcommands. | 1.1.0 |
| [`COMMAND`](command.md) | Every command, each as [name, arity, [flags], first-key, last-key, key-step, [@categories], [], [], []]. | 1.1.0 |
| [`CONFIG`](config.md) | CONFIG and its subcommands. | 1.1.0 |
| [`DBSIZE`](dbsize.md) | Return the number of keys in the current database | 1.1.0 |
| [`DEBUG`](debug.md) | Accepted and ignored for redis-cli compatibility | 1.1.0 |
| [`ECHO`](echo.md) | Returns the message back | 1.1.0 |
| [`FLUSHALL`](flushall.md) | Delete all keys in all databases | 1.1.0 |
| [`FLUSHDB`](flushdb.md) | Delete all keys in the current database | 1.1.0 |
| [`HELLO`](hello.md) | Switch the connection to RESP2 or RESP3 and return the server's details (server, version, proto, id, mode, role, modules) — a map under RESP3. | 1.1.0 |
| [`INFO`](info.md) | Return server info; sections include server, keyspace, replication, errorstats (per-error reply counters), all, etc. | 1.1.0 |
| [`LASTSAVE`](lastsave.md) | Return the Unix timestamp of the last successful save | 1.1.0 |
| [`LOLWUT`](lolwut.md) | Return ASCII art and the server version | 1.1.0 |
| [`MEMORY`](memory.md) | MEMORY and its subcommands. | 1.1.0 |
| [`MONITOR`](monitor.md) | Stream every command executed on the server to this connection in real time. | 1.1.0 |
| [`PSYNC`](psync.md) | Internal replication sync command | 1.1.0 |
| [`REPLCONF`](replconf.md) | Internal replication configuration command | 1.1.0 |
| [`REPLICAOF`](replicaof.md) | Configure this instance as a replica, or promote to master. | 1.1.0 |
| [`ROLE`](role.md) | Return the replication role: master or slave, with offset and replica list | 1.1.0 |
| [`SAVE`](save.md) | Synchronously save a snapshot to dump.kdb | 1.1.0 |
| [`SELECT`](select.md) | Switch to a database (0–15) | 1.1.0 |
| [`SHUTDOWN`](shutdown.md) | Gracefully stop the server. | 1.1.0 |
| [`SLAVEOF`](slaveof.md) | Alias for REPLICAOF | 1.1.0 |
| [`SYNC`](sync.md) | Old-style full synchronisation for a replica: the snapshot, then the command stream | 1.1.0 |
| [`TIME`](time.md) | Return [unix_seconds, microseconds_within_second] as two bulk strings; uses real wall clock | 1.1.0 |
| [`WAIT`](wait.md) | Block until numreplicas replicas have acknowledged all preceding writes, or timeout milliseconds elapse; returns the number of replicas that acked | 1.1.0 |
| [`WAITAOF`](waitaof.md) | Block until the local AOF has fsynced all preceding writes, or timeout milliseconds elapse; returns [local_fsynced, replica_fsynced] | 1.1.0 |

## Set

| Command | Summary | Since |
|---|---|---|
| [`SADD`](sadd.md) | Adds members to the set at key. | 1.1.0 |
| [`SCARD`](scard.md) | Returns the number of members of the set at key. | 1.1.0 |
| [`SDIFF`](sdiff.md) | Returns the members of the first set that are in none of the others. | 1.1.0 |
| [`SDIFFCARD`](sdiffcard.md) | Returns how many members the difference of the given sets has, without returning them: a command of Redis 8.10. | 1.1.0 |
| [`SDIFFSTORE`](sdiffstore.md) | Stores the difference of the given sets, as SDIFF computes it, at destination, replacing whatever was there, and its expiry. | 1.1.0 |
| [`SINTER`](sinter.md) | Returns the members that are in every one of the given sets. | 1.1.0 |
| [`SINTERCARD`](sintercard.md) | Returns how many members the intersection of the given sets has, without returning them. | 1.1.0 |
| [`SINTERSTORE`](sinterstore.md) | Stores the intersection of the given sets, as SINTER computes it, at destination, replacing whatever was there, and its expiry. | 1.1.0 |
| [`SISMEMBER`](sismember.md) | Tells whether member is in the set at key. | 1.1.0 |
| [`SMEMBERS`](smembers.md) | Returns every member of the set at key, in no particular order. | 1.1.0 |
| [`SMISMEMBER`](smismember.md) | Tells, for each of several members, whether it is in the set at key. | 1.1.0 |
| [`SMOVE`](smove.md) | Moves member from the set at source to the set at destination, in one step. | 1.1.0 |
| [`SPOP`](spop.md) | Removes and returns members of the set at key, picked at random. | 1.1.0 |
| [`SRANDMEMBER`](srandmember.md) | Returns members of the set at key, picked at random, without removing them. | 1.1.0 |
| [`SREM`](srem.md) | Removes members from the set at key. | 1.1.0 |
| [`SSCAN`](sscan.md) | Goes through the members of the set at key a page at a time, as SCAN goes through keys. | 1.1.0 |
| [`SUNION`](sunion.md) | Returns the members that are in any of the given sets. | 1.1.0 |
| [`SUNIONCARD`](sunioncard.md) | Returns how many members the union of the given sets has, without returning them: a command of Redis 8.10. | 1.1.0 |
| [`SUNIONSTORE`](sunionstore.md) | Stores the union of the given sets at destination, replacing whatever was there, and its expiry. | 1.1.0 |

## Sorted set

| Command | Summary | Since |
|---|---|---|
| [`BZMPOP`](bzmpop.md) | Blocking ZMPOP | 1.1.0 |
| [`BZPOPMAX`](bzpopmax.md) | Blocking ZPOPMAX; blocks until a member is available | 1.1.0 |
| [`BZPOPMIN`](bzpopmin.md) | Blocking ZPOPMIN; blocks until a member is available | 1.1.0 |
| [`ZADD`](zadd.md) | Add or update members with scores; NX=only add new, XX=only update existing, GT/LT=conditional update, CH=return changed count, INCR=treat as increment | 1.1.0 |
| [`ZCARD`](zcard.md) | Return the number of members | 1.1.0 |
| [`ZCOUNT`](zcount.md) | Count members with scores in range; supports ( for exclusive bounds and -inf/+inf | 1.1.0 |
| [`ZDIFF`](zdiff.md) | Return members in first set not in subsequent sets | 1.1.0 |
| [`ZDIFFSTORE`](zdiffstore.md) | Store ZDIFF result | 1.1.0 |
| [`ZINCRBY`](zincrby.md) | Increment a member's score; returns new score | 1.1.0 |
| [`ZINTER`](zinter.md) | Return intersection of sorted sets; AGGREGATE COUNT (Redis 8.8) scores each member by the number of input sets it is in | 1.1.0 |
| [`ZINTERCARD`](zintercard.md) | Return cardinality of intersection | 1.1.0 |
| [`ZINTERSTORE`](zinterstore.md) | Store ZINTER result | 1.1.0 |
| [`ZLEXCOUNT`](zlexcount.md) | Count members in lexicographical range; bounds use [ (inclusive) or ( (exclusive); - and + for open ends | 1.1.0 |
| [`ZMPOP`](zmpop.md) | Pop from first non-empty sorted set | 1.1.0 |
| [`ZMSCORE`](zmscore.md) | Return scores for multiple members | 1.1.0 |
| [`ZPOPMAX`](zpopmax.md) | Remove and return highest-scoring members | 1.1.0 |
| [`ZPOPMIN`](zpopmin.md) | Remove and return lowest-scoring members | 1.1.0 |
| [`ZRANDMEMBER`](zrandmember.md) | Return random members; positive count = distinct, negative = with repetition | 1.1.0 |
| [`ZRANGE`](zrange.md) | Return members in range; unified command supporting index, score, and lex modes | 1.1.0 |
| [`ZRANGEBYLEX`](zrangebylex.md) | Return members in lexicographical range | 1.1.0 |
| [`ZRANGEBYSCORE`](zrangebyscore.md) | Return members by score range (legacy alias) | 1.1.0 |
| [`ZRANGESTORE`](zrangestore.md) | Store result of ZRANGE into a key; returns count stored | 1.1.0 |
| [`ZRANK`](zrank.md) | Return 0-based rank in ascending score order | 1.1.0 |
| [`ZREM`](zrem.md) | Remove members; returns count removed | 1.1.0 |
| [`ZREMRANGEBYLEX`](zremrangebylex.md) | Remove members in lexicographical range | 1.1.0 |
| [`ZREMRANGEBYRANK`](zremrangebyrank.md) | Remove members by index range | 1.1.0 |
| [`ZREMRANGEBYSCORE`](zremrangebyscore.md) | Remove members with scores in range | 1.1.0 |
| [`ZREVRANGE`](zrevrange.md) | Return members by index descending (legacy alias) | 1.1.0 |
| [`ZREVRANGEBYLEX`](zrevrangebylex.md) | Return members in reverse lexicographical range | 1.1.0 |
| [`ZREVRANGEBYSCORE`](zrevrangebyscore.md) | Return members by score range descending (legacy alias) | 1.1.0 |
| [`ZREVRANK`](zrevrank.md) | Return 0-based rank in descending score order | 1.1.0 |
| [`ZSCAN`](zscan.md) | Cursor-based iteration over members and scores; NOSCORES returns members only. | 1.1.0 |
| [`ZSCORE`](zscore.md) | Return the score of a member, or nil | 1.1.0 |
| [`ZUNION`](zunion.md) | Return union of sorted sets; AGGREGATE COUNT (Redis 8.8) scores each member by the number of input sets it is in | 1.1.0 |
| [`ZUNIONSTORE`](zunionstore.md) | Store ZUNION result | 1.1.0 |

## Stream

| Command | Summary | Since |
|---|---|---|
| [`XACK`](xack.md) | Acknowledge processed entries; removes from PEL | 1.1.0 |
| [`XACKDEL`](xackdel.md) | Acknowledge and delete entries in one step (Redis 8.2). | 1.1.0 |
| [`XADD`](xadd.md) | Append an entry; * auto-generates ID as ms-seq; NOMKSTREAM skips creation if key absent; MAXLEN/MINID trim the stream after insert, and KEEPREF / DELREF / ACKED say what trimming does with entries co… | 1.1.0 |
| [`XAUTOCLAIM`](xautoclaim.md) | Scan and claim idle pending entries starting from start | 1.1.0 |
| [`XCFGSET`](xcfgset.md) | Set per-stream configuration; supported fields: MAX-ENTRIES n (persistent trim policy applied on every XADD, 0 clears the policy), MAX-DELETED-ENTRY-ID id (advance the tracked max deleted ID, never m… | 1.1.0 |
| [`XCLAIM`](xclaim.md) | Claim ownership of pending entries idle longer than min-idle-time | 1.1.0 |
| [`XDEL`](xdel.md) | Delete entries by ID; returns count deleted | 1.1.0 |
| [`XDELEX`](xdelex.md) | Delete entries with control over consumer-group references (Redis 8.2). | 1.1.0 |
| [`XGROUP`](xgroup.md) | XGROUP and its subcommands. | 1.1.0 |
| [`XINFO`](xinfo.md) | XINFO and its subcommands. | 1.1.0 |
| [`XLEN`](xlen.md) | Return the number of entries | 1.1.0 |
| [`XNACK`](xnack.md) | Release pending entries back to the group PEL without acknowledging, for immediate re-delivery. | 1.1.0 |
| [`XPENDING`](xpending.md) | Return pending entry summary or detail list | 1.1.0 |
| [`XRANGE`](xrange.md) | Return entries with IDs in [start, end]; - and + are open bounds; bare ms expands to ms-0 / ms-MAXSEQ | 1.1.0 |
| [`XREAD`](xread.md) | Read new entries across multiple streams; $ means entries added after this call and + the last entry; BLOCK suspends until new data arrives or timeout. | 1.1.0 |
| [`XREADGROUP`](xreadgroup.md) | Read new (>) or pending (specific ID) entries for a consumer; NOACK skips PEL tracking. | 1.1.0 |
| [`XREVRANGE`](xrevrange.md) | Same as XRANGE but in reverse order | 1.1.0 |
| [`XSETID`](xsetid.md) | Set the stream's last-generated ID and metadata | 1.1.0 |
| [`XTRIM`](xtrim.md) | Trim stream by length or minimum ID. | 1.1.0 |

## String

| Command | Summary | Since |
|---|---|---|
| [`APPEND`](append.md) | Appends value to the string at key. | 1.1.0 |
| [`DECR`](decr.md) | Subtracts 1 from the integer stored at key. | 1.1.0 |
| [`DECRBY`](decrby.md) | Subtracts decrement, a signed 64-bit integer, from the integer stored at key. | 1.1.0 |
| [`DELEX`](delex.md) | Deletes key, optionally only if its string value, or the value's digest, matches. | 1.1.0 |
| [`DIGEST`](digest.md) | Returns a digest of the string at key: the XXH3 64-bit hash of the value, as 16 hexadecimal digits. | 1.1.0 |
| [`GET`](get.md) | Returns the string stored at key. | 1.1.0 |
| [`GETDEL`](getdel.md) | Returns the string at key and deletes the key, in one step. | 1.1.0 |
| [`GETEX`](getex.md) | Returns the string at key and, optionally, changes its expiry. | 1.1.0 |
| [`GETRANGE`](getrange.md) | Returns the bytes of the string at key from offset start to offset end, both included. | 1.1.0 |
| [`GETSET`](getset.md) | Sets key to value and returns the value it held before, in one step. | 1.1.0 |
| [`INCR`](incr.md) | Adds 1 to the integer stored at key. | 1.1.0 |
| [`INCRBY`](incrby.md) | Adds increment, a signed 64-bit integer, to the integer stored at key. | 1.1.0 |
| [`INCRBYFLOAT`](incrbyfloat.md) | Adds increment, a floating-point number, to the number stored at key. | 1.1.0 |
| [`INCREX`](increx.md) | Increments the number at key with bounds, and optionally sets its expiry, in one step. | 1.1.0 |
| [`LCS`](lcs.md) | Finds the longest common subsequence of the strings at key1 and key2: the longest run of characters found in both, in the same order, not necessarily next to each other. | 1.1.0 |
| [`MGET`](mget.md) | Returns the values of several keys. | 1.1.0 |
| [`MSET`](mset.md) | Sets several keys to string values in one step. | 1.1.0 |
| [`MSETEX`](msetex.md) | Sets several keys in one step, with one expiry for all of them, and optionally only if they all exist or none does. | 1.1.0 |
| [`MSETNX`](msetnx.md) | Sets several keys to string values only if none of them exists. | 1.1.0 |
| [`PSETEX`](psetex.md) | Sets key to value and makes it expire after milliseconds. | 1.1.0 |
| [`SET`](set.md) | Stores a string at key, replacing whatever the key held, of any type. | 1.1.0 |
| [`SETEX`](setex.md) | Sets key to value and makes it expire after seconds. | 1.1.0 |
| [`SETNX`](setnx.md) | Sets key to value only if the key does not exist. | 1.1.0 |
| [`SETRANGE`](setrange.md) | Overwrites the string at key from byte offset on with value. | 1.1.0 |
| [`STRLEN`](strlen.md) | Returns the length, in bytes, of the string at key. | 1.1.0 |
| [`SUBSTR`](substr.md) | Another name for GETRANGE, kept for old clients. | 1.1.0 |

## Time series

| Command | Summary | Since |
|---|---|---|
| [`TS.ADD`](ts.add.md) | Append a sample. | 1.1.0 |
| [`TS.ALTER`](ts.alter.md) | Update retention, chunk size, duplicate policy, or labels. | 1.1.0 |
| [`TS.CREATE`](ts.create.md) | Create a new time series. | 1.1.0 |
| [`TS.CREATERULE`](ts.createrule.md) | Create a compaction rule from source to destination. | 1.1.0 |
| [`TS.DECRBY`](ts.decrby.md) | Add a new sample equal to the last sample's value minus the given decrement | 1.1.0 |
| [`TS.DEL`](ts.del.md) | Delete all samples in the inclusive timestamp range. | 1.1.0 |
| [`TS.DELETERULE`](ts.deleterule.md) | Delete a compaction rule | 1.1.0 |
| [`TS.GET`](ts.get.md) | Return the sample with the highest timestamp. | 1.1.0 |
| [`TS.INCRBY`](ts.incrby.md) | Add a new sample equal to the last sample's value plus the given increment. | 1.1.0 |
| [`TS.INFO`](ts.info.md) | Return metadata for a series: totalSamples, firstTimestamp, lastTimestamp, retentionTime, chunkSize, duplicatePolicy, labels, rules | 1.1.0 |
| [`TS.MADD`](ts.madd.md) | Append samples to one or more series in a single call. | 1.1.0 |
| [`TS.MGET`](ts.mget.md) | Return the latest sample from each series matching the label filters | 1.1.0 |
| [`TS.MRANGE`](ts.mrange.md) | Query a range across multiple series matching label filters, in forward order. | 1.1.0 |
| [`TS.MREVRANGE`](ts.mrevrange.md) | Query a range across multiple series in reverse order. | 1.1.0 |
| [`TS.NRANGE`](ts.nrange.md) | Query the same range over several named series and join the results by timestamp (Redis 8.10): one row per timestamp any of them reports, with a value — or NaN — for each key, in the order given | 1.1.0 |
| [`TS.NREVRANGE`](ts.nrevrange.md) | TS.NRANGE in reverse order | 1.1.0 |
| [`TS.QUERYINDEX`](ts.queryindex.md) | Return all time series keys matching the given label filters. | 1.1.0 |
| [`TS.QUERYLABELS`](ts.querylabels.md) | The label names in use, or the values of one label, across the series matching the filters (Redis 8.10) | 1.1.0 |
| [`TS.RANGE`](ts.range.md) | Query a range in forward (ascending) order. | 1.1.0 |
| [`TS.READ`](ts.read.md) | The samples at or after a timestamp, oldest first (Redis 8.10) — for following a series. | 1.1.0 |
| [`TS.REVRANGE`](ts.revrange.md) | Query a range in reverse (descending) order. | 1.1.0 |

## Transaction

| Command | Summary | Since |
|---|---|---|
| [`DISCARD`](discard.md) | Discard all queued commands and exit transaction mode | 1.1.0 |
| [`EXEC`](exec.md) | Execute all queued commands atomically; returns nil if a WATCHed key was modified | 1.1.0 |
| [`MULTI`](multi.md) | Begin a transaction; subsequent commands are queued and return +QUEUED | 1.1.0 |
| [`UNWATCH`](unwatch.md) | Clear all watched keys for the current connection | 1.1.0 |
| [`WATCH`](watch.md) | Mark keys for optimistic locking; must be called before MULTI | 1.1.0 |

## Vector search

| Command | Summary | Since |
|---|---|---|
| [`FT.AGGREGATE`](ft.aggregate.md) | Aggregate the documents a query matches. | 1.1.0 |
| [`FT.ALIASADD`](ft.aliasadd.md) | Create an alias pointing to an existing index; AOF-logged | 1.1.0 |
| [`FT.ALIASDEL`](ft.aliasdel.md) | Remove an alias; AOF-logged | 1.1.0 |
| [`FT.ALIASLIST`](ft.aliaslist.md) | The aliases that point to index (Redis 8.10) | 1.1.0 |
| [`FT.ALIASUPDATE`](ft.aliasupdate.md) | Update an alias; overwrites if it already exists; AOF-logged | 1.1.0 |
| [`FT.ALTER`](ft.alter.md) | Add new fields to an existing index schema. | 1.1.0 |
| [`FT.CONFIG`](ft.config.md) | FT.CONFIG and its subcommands. | 1.1.0 |
| [`FT.CREATE`](ft.create.md) | Create a search index; supported field types: TEXT, TAG, NUMERIC, VECTOR; backfills existing keys on creation. | 1.1.0 |
| [`FT.CURSOR`](ft.cursor.md) | FT.CURSOR and its subcommands. | 1.1.0 |
| [`FT.DEBUG`](ft.debug.md) | FT.DEBUG and its subcommands. | 1.1.0 |
| [`FT.DICTADD`](ft.dictadd.md) | Add terms to a named global dictionary; returns count of newly added terms; AOF-logged | 1.1.0 |
| [`FT.DICTDEL`](ft.dictdel.md) | Remove terms from a dictionary; returns count removed; AOF-logged | 1.1.0 |
| [`FT.DICTDUMP`](ft.dictdump.md) | Return all terms in a dictionary, sorted alphabetically | 1.1.0 |
| [`FT.DROPINDEX`](ft.dropindex.md) | Delete an index definition; does not delete the underlying data keys | 1.1.0 |
| [`FT.EXPLAIN`](ft.explain.md) | The query's plan as Redis writes one: INTERSECT { … }, UNION { … }, NOT, OPTIONAL, TAG:@field { … }, NUMERIC {lo <= @field <= hi}, VECTOR { … }, one clause to a line. | 1.1.0 |
| [`FT.EXPLAINCLI`](ft.explaincli.md) | The same plan as an array of its lines | 1.1.0 |
| [`FT.HYBRID`](ft.hybrid.md) | Combined text + vector search with score fusion. | 1.1.0 |
| [`FT.INFO`](ft.info.md) | Return index metadata: name, type, prefixes, field schemas, field count. | 1.1.0 |
| [`FT.PROFILE`](ft.profile.md) | Runs the query and returns [reply, profile] (a map with Results and Profile under RESP3). | 1.1.0 |
| [`FT.SEARCH`](ft.search.md) | Search an index; supports pure KNN (*=>[KNN k @field $param AS alias]), pure text/filter queries (@field:token, @field:{tag}, @field:[lo hi], *), and hybrid pre-filter KNN; TEXT fields use BM25 scori… | 1.1.0 |
| [`FT.SPELLCHECK`](ft.spellcheck.md) | Return spelling suggestions for unrecognised query terms. | 1.1.0 |
| [`FT.SYNDUMP`](ft.syndump.md) | Return all synonym groups as a flat term → [group_id] mapping | 1.1.0 |
| [`FT.SYNUPDATE`](ft.synupdate.md) | Create or update a synonym group; terms in a group are treated as equivalent; AOF-logged | 1.1.0 |
| [`FT.TAGVALS`](ft.tagvals.md) | Return all distinct values stored in a TAG field across indexed keys; sorted alphabetically; splits on \| and , | 1.1.0 |
| [`FT._LIST`](ft._list.md) | Return a list of all index names | 1.1.0 |

## Vector set

| Command | Summary | Since |
|---|---|---|
| [`VADD`](vadd.md) | Add or update an element with its vector; FP32 accepts raw little-endian bytes, VALUES n accepts space-separated floats; returns 1 if new, 0 if updated; AOF-logged | 1.1.0 |
| [`VCARD`](vcard.md) | Return the number of elements in the set; 0 if key does not exist | 1.1.0 |
| [`VDIM`](vdim.md) | Return the vector dimension; nil if key does not exist | 1.1.0 |
| [`VEMB`](vemb.md) | Return the vector as an array of float strings; with RAW, return raw little-endian FP32 bytes | 1.1.0 |
| [`VGETATTR`](vgetattr.md) | Return the JSON attributes string attached to an element; nil if none | 1.1.0 |
| [`VINFO`](vinfo.md) | Return metadata: vector-dim, vector-count, quant-type, index-type, max-level | 1.1.0 |
| [`VISMEMBER`](vismember.md) | Return 1 if element exists, 0 otherwise | 1.1.0 |
| [`VLINKS`](vlinks.md) | Return nearest neighbours of an element (up to 16) as a single-layer array; approximated via brute-force cosine similarity | 1.1.0 |
| [`VRANDMEMBER`](vrandmember.md) | Return random elements; positive count returns distinct elements up to set size; negative count returns \|count\| elements with repetition allowed | 1.1.0 |
| [`VRANGE`](vrange.md) | Return elements in lexicographical range of element names; bounds follow ZRANGEBYLEX syntax: [inclusive, (exclusive, - for start, + for end | 1.1.0 |
| [`VREM`](vrem.md) | Remove one or more elements; returns count removed; AOF-logged | 1.1.0 |
| [`VSETATTR`](vsetattr.md) | Attach a JSON attributes string to an element; pass empty string "" to remove; AOF-logged | 1.1.0 |
| [`VSIM`](vsim.md) | Return elements ordered by cosine similarity to the query vector; ELE queries by an existing element's vector; scores are similarities computed using the set's stored distance metric (1.0 = identical… | 1.1.0 |
