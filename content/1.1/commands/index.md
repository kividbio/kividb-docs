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
| [`ACL`](acl.md) | Manages users and what each may do: which commands it may run, which keys it may read or write, which channels it may use. | 1.1.0 |
| [`AUTH`](auth.md) | Logs the connection in as a user: AUTH username password, or, with a password only, as the default user. | 1.1.0 |

## Array

| Command | Summary | Since |
|---|---|---|
| [`ARCOUNT`](arcount.md) | Returns the number of filled slots; 0 for a missing key. | 1.1.0 |
| [`ARDEL`](ardel.md) | Empties the slots at the given indexes. | 1.1.0 |
| [`ARDELRANGE`](ardelrange.md) | Empties the slots in one or more ranges, each from start to end, both included. | 1.1.0 |
| [`ARGET`](arget.md) | Returns the value at index, or nil for an empty slot. | 1.1.0 |
| [`ARGETRANGE`](argetrange.md) | Returns every slot from start to end, both included, nil for empty ones. | 1.1.0 |
| [`ARGREP`](argrep.md) | Returns the indexes of the slots from start to end whose values match. | 1.1.0 |
| [`ARINFO`](arinfo.md) | Returns the array's filled slots (count), its len, the insert cursor (next-insert-index), and how it is laid out in memory: its slices of slice-size slots, and the directories that find them. | 1.1.0 |
| [`ARINSERT`](arinsert.md) | Writes values at the array's insert cursor, moving the cursor on one slot per value. | 1.1.0 |
| [`ARLASTITEMS`](arlastitems.md) | Returns the count slots before the insert cursor, oldest first, or newest first with REV, nil for empty ones. | 1.1.0 |
| [`ARLEN`](arlen.md) | Returns the highest filled index plus one; 0 for a missing key. | 1.1.0 |
| [`ARMGET`](armget.md) | Returns the values at several indexes, in the order given, nil for empty slots. | 1.1.0 |
| [`ARMSET`](armset.md) | Sets values at several indexes, in any order, in one call. | 1.1.0 |
| [`ARNEXT`](arnext.md) | Returns the index the next ARINSERT will use: 0 for a missing key, nil once the cursor has run past the last index. | 1.1.0 |
| [`AROP`](arop.md) | Computes over the filled slots from start to end. | 1.1.0 |
| [`ARRING`](arring.md) | Writes values into a ring buffer of size slots: the cursor wraps around at size, so newer values overwrite the oldest. | 1.1.0 |
| [`ARSCAN`](arscan.md) | Returns the filled slots from start to end, skipping empty ones, as [index, value] pairs; in reverse with start greater than end. | 1.1.0 |
| [`ARSEEK`](arseek.md) | Moves the insert cursor to index. | 1.1.0 |
| [`ARSET`](arset.md) | Sets values in the array at key from index on, one slot each. | 1.1.0 |

## Bitmap

| Command | Summary | Since |
|---|---|---|
| [`BITCOUNT`](bitcount.md) | Counts the bits set to 1 in the string at key, or in a part of it. | 1.1.0 |
| [`BITFIELD`](bitfield.md) | Reads, writes and increments integers of any width from 1 to 64 bits, stored at any bit offset of the string at key, in one command. | 1.1.0 |
| [`BITFIELD_RO`](bitfield_ro.md) | BITFIELD with GET only: it only reads, so it can be sent to a read-only replica. | 1.1.0 |
| [`BITOP`](bitop.md) | Combines the strings at the source keys bit by bit and stores the result at destkey. | 1.1.0 |
| [`BITPOS`](bitpos.md) | Returns the position of the first bit set to bit (0 or 1) in the string at key, or in a part of it. | 1.1.0 |
| [`GETBIT`](getbit.md) | Returns the bit at offset in the string at key. | 1.1.0 |
| [`SETBIT`](setbit.md) | Sets or clears the bit at offset in the string at key. | 1.1.0 |

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
| [`GEOADD`](geoadd.md) | Adds places, each a longitude, a latitude and a name, to the geospatial index at key: a sorted set whose scores encode positions, so that it can be searched by distance. | 1.1.0 |
| [`GEODELBYMEMBER`](geodelbymember.md) | COMMAND lists GEODELBYMEMBER, but KiviDB 1.1 does not have it: calling it replies ERR unknown command 'GEODELBYMEMBER'. | 1.1.0 |
| [`GEODIST`](geodist.md) | Returns the distance between two members of the geospatial index at key, in metres, or in KM, FT or MI. | 1.1.0 |
| [`GEOHASH`](geohash.md) | Returns the geohash of members of the geospatial index at key: the standard 11-character base32 string, which other geohash tools read. | 1.1.0 |
| [`GEOPOS`](geopos.md) | Returns the longitude and latitude of members of the geospatial index at key. | 1.1.0 |
| [`GEORADIUS`](georadius.md) | Returns the members of the geospatial index at key within radius of a longitude and latitude. | 1.1.0 |
| [`GEORADIUSBYMEMBER`](georadiusbymember.md) | GEORADIUS centred on a member of the index, not a position. | 1.1.0 |
| [`GEORADIUSBYMEMBER_RO`](georadiusbymember_ro.md) | GEORADIUSBYMEMBER without STORE or STOREDIST, for read-only replicas. | 1.1.0 |
| [`GEORADIUS_RO`](georadius_ro.md) | GEORADIUS without STORE or STOREDIST: it only reads, so it can be sent to a read-only replica. | 1.1.0 |
| [`GEOSEARCH`](geosearch.md) | Returns the members of the geospatial index at key within a circle or a box. | 1.1.0 |
| [`GEOSEARCHSTORE`](geosearchstore.md) | Stores the members GEOSEARCH would return at destination. | 1.1.0 |

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
| [`PFADD`](pfadd.md) | Adds elements to the HyperLogLog at key: a structure of fixed size that estimates how many different elements it has been given, however many that is. | 1.1.0 |
| [`PFCOUNT`](pfcount.md) | Returns the estimated number of different elements added to the HyperLogLog at key. | 1.1.0 |
| [`PFDEBUG`](pfdebug.md) | Inspects or resets a HyperLogLog. | 1.1.0 |
| [`PFMERGE`](pfmerge.md) | Merges the HyperLogLogs at the source keys into destkey, so that it estimates their union. | 1.1.0 |
| [`PFSELFTEST`](pfselftest.md) | Runs KiviDB's checks of its HyperLogLog code: an empty one counts 0, 10,000 elements are estimated within 2%, and registers read back as written. | 1.1.0 |

## Json

| Command | Summary | Since |
|---|---|---|
| [`JSON.ARRAPPEND`](json.arrappend.md) | Appends values, each JSON text, to each array path matches. | 1.1.0 |
| [`JSON.ARRINDEX`](json.arrindex.md) | Returns the index of the first element equal to value, JSON text, in each array path matches, from start to stop. | 1.1.0 |
| [`JSON.ARRINSERT`](json.arrinsert.md) | Inserts values, each JSON text, before index in each array path matches. | 1.1.0 |
| [`JSON.ARRLEN`](json.arrlen.md) | Returns the length of each array path matches. | 1.1.0 |
| [`JSON.ARRPOP`](json.arrpop.md) | Removes and returns an element from each array path matches: the last one, or the one at index. | 1.1.0 |
| [`JSON.ARRTRIM`](json.arrtrim.md) | Keeps only the elements from start to stop, both included, in each array path matches. | 1.1.0 |
| [`JSON.CLEAR`](json.clear.md) | Empties each array and object path matches, and sets each number it matches to 0. | 1.1.0 |
| [`JSON.DEBUG`](json.debug.md) | Reports on JSON documents. | 1.1.0 |
| [`JSON.DEL`](json.del.md) | Deletes the values path matches in the JSON document at key. | 1.1.0 |
| [`JSON.FORGET`](json.forget.md) | Another name for JSON.DEL. | 1.1.0 |
| [`JSON.GET`](json.get.md) | Returns values from the JSON document at key, as JSON text. | 1.1.0 |
| [`JSON.MERGE`](json.merge.md) | Merges value into each value path matches, as an RFC 7396 merge patch: members are merged into objects, null deletes a member, and anything else replaces. | 1.1.0 |
| [`JSON.MGET`](json.mget.md) | Evaluates path in the JSON documents at several keys. | 1.1.0 |
| [`JSON.MSET`](json.mset.md) | JSON.SET for several key-path-value triples at once. | 1.1.0 |
| [`JSON.NUMINCRBY`](json.numincrby.md) | Adds number to each number path matches. | 1.1.0 |
| [`JSON.NUMMULTBY`](json.nummultby.md) | Multiplies each number path matches by number, with the same replies as JSON.NUMINCRBY. | 1.1.0 |
| [`JSON.OBJKEYS`](json.objkeys.md) | Returns the member names of each object path matches, in the order they were added. | 1.1.0 |
| [`JSON.OBJLEN`](json.objlen.md) | Returns the number of members of each object path matches. | 1.1.0 |
| [`JSON.RESP`](json.resp.md) | Returns each value path matches in RESP rather than JSON text: null as nil, booleans as true and false, integers as integers, other numbers and strings as bulk strings, an array as [ followed by its… | 1.1.0 |
| [`JSON.SET`](json.set.md) | Sets the value at path in the JSON document at key to value, which is JSON text. | 1.1.0 |
| [`JSON.STRAPPEND`](json.strappend.md) | Appends a JSON string to each string path matches. | 1.1.0 |
| [`JSON.STRLEN`](json.strlen.md) | Returns the length of each string path matches; nil for a match that is not a string. | 1.1.0 |
| [`JSON.TOGGLE`](json.toggle.md) | Flips each boolean path matches. | 1.1.0 |
| [`JSON.TYPE`](json.type.md) | Returns the type of each value path matches: object, array, string, integer, number, boolean or null. | 1.1.0 |

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
| [`HOTKEYS`](hotkeys.md) | Finds the keys that use the most CPU time, or the most network bytes, during a session started with HOTKEYS START. | 1.1.0 |
| [`LATENCY`](latency.md) | The latency monitor: it records, for each kind of event, the times it took longer than latency-monitor-threshold milliseconds, which is 0, off, by default. | 1.1.0 |
| [`SLOWLOG`](slowlog.md) | The slow log: the commands that took longer than slowlog-log-slower-than microseconds to run, up to slowlog-max-len entries (128 by default). | 1.1.0 |

## Pub sub

| Command | Summary | Since |
|---|---|---|
| [`PING`](ping.md) | Checks that the server answers. | 1.1.0 |
| [`PSUBSCRIBE`](psubscribe.md) | Subscribes this connection to every channel matching a glob-style pattern. | 1.1.0 |
| [`PUBLISH`](publish.md) | Sends message to every client subscribed to channel, with SUBSCRIBE, or to a pattern that matches it, with PSUBSCRIBE. | 1.1.0 |
| [`PUBSUB`](pubsub.md) | Reports on the channels and patterns clients are subscribed to. | 1.1.0 |
| [`PUNSUBSCRIBE`](punsubscribe.md) | Unsubscribes this connection from patterns, or from all of them if none is given. | 1.1.0 |
| [`QUIT`](quit.md) | Asks the server to close the connection, after replying OK. | 1.1.0 |
| [`RESET`](reset.md) | Puts the connection back as it was when it was opened: unsubscribed from everything, out of any transaction and with no keys watched, on database 0, speaking RESP2, with no name and no client-side ca… | 1.1.0 |
| [`SPUBLISH`](spublish.md) | Sends message to the clients subscribed to the shard channel shardchannel with SSUBSCRIBE. | 1.1.0 |
| [`SSUBSCRIBE`](ssubscribe.md) | Subscribes this connection to shard channels. | 1.1.0 |
| [`SUBSCRIBE`](subscribe.md) | Subscribes this connection to channels. | 1.1.0 |
| [`SUNSUBSCRIBE`](sunsubscribe.md) | Unsubscribes this connection from shard channels, or from all of them if none is given. | 1.1.0 |
| [`UNSUBSCRIBE`](unsubscribe.md) | Unsubscribes this connection from channels, or from all of them if none is given. | 1.1.0 |

## Scripting

| Command | Summary | Since |
|---|---|---|
| [`EVAL`](eval.md) | Runs a Lua script on the server, as one step: no other client's command starts while it runs. | 1.1.0 |
| [`EVALSHA`](evalsha.md) | Runs a script the server already has, named by its SHA1 digest, as SCRIPT LOAD returns it, or as a previous EVAL cached it. | 1.1.0 |
| [`EVALSHA_RO`](evalsha_ro.md) | EVALSHA for a script that only reads, as EVAL_RO is. | 1.1.0 |
| [`EVAL_RO`](eval_ro.md) | EVAL for a script that only reads: a command in it that writes fails. | 1.1.0 |
| [`FCALL`](fcall.md) | Calls a function of a library loaded with FUNCTION LOAD. | 1.1.0 |
| [`FCALL_RO`](fcall_ro.md) | FCALL for a function registered with the no-writes flag; any other is refused. | 1.1.0 |
| [`FUNCTION`](function.md) | Manages libraries of functions, which FCALL calls. | 1.1.0 |
| [`SCRIPT`](script.md) | Manages the cache of scripts EVAL and SCRIPT LOAD fill, and the script running. | 1.1.0 |

## Server

| Command | Summary | Since |
|---|---|---|
| [`BACKUP`](backup.md) | Takes a consistent backup of the dataset while the server keeps serving: a snapshot as of the start, then the writes that follow, up to the moment it is sealed. | 1.1.0 |
| [`BGREWRITEAOF`](bgrewriteaof.md) | Rewrites the append-only file in the background, as the shortest file that rebuilds the dataset. | 1.1.0 |
| [`BGSAVE`](bgsave.md) | Writes a snapshot of the dataset to dump.kdb in the background, and replies at once. | 1.1.0 |
| [`CLIENT`](client.md) | Inspects and manages client connections. | 1.1.0 |
| [`COMMAND`](command.md) | Returns every command, each as an array: its name, its arity (a negative number is a minimum), its flags, the positions of its first and last key and the step between them, and its ACL categories. | 1.1.0 |
| [`CONFIG`](config.md) | Reads and changes the server's settings at runtime. | 1.1.0 |
| [`DBSIZE`](dbsize.md) | Returns the number of keys in the current database. | 1.1.0 |
| [`DEBUG`](debug.md) | Accepted for compatibility with Redis tools. | 1.1.0 |
| [`ECHO`](echo.md) | Returns message. | 1.1.0 |
| [`FAILOVER`](failover.md) | Refused. | 1.1.0 |
| [`FLUSHALL`](flushall.md) | Deletes every key of every database. | 1.1.0 |
| [`FLUSHDB`](flushdb.md) | Deletes every key of the current database. | 1.1.0 |
| [`HELLO`](hello.md) | Switches the connection to RESP2 or RESP3, and returns the server's details: its name, version, protocol, connection ID, mode, role and modules, as a map under RESP3. | 1.1.0 |
| [`INFO`](info.md) | Returns information and statistics about the server, as field:value lines in sections. | 1.1.0 |
| [`LASTSAVE`](lastsave.md) | Returns the Unix time of the last snapshot saved, 0 if none. | 1.1.0 |
| [`LOLWUT`](lolwut.md) | Returns a small drawing and the server's version. | 1.1.0 |
| [`MEMORY`](memory.md) | Reports on memory use. | 1.1.0 |
| [`MODULE`](module.md) | KiviDB does not load modules. | 1.1.0 |
| [`MONITOR`](monitor.md) | Streams every command the server runs, from any client, to this connection, each as a line: the time, the database and client address, and the command and its arguments. | 1.1.0 |
| [`PSYNC`](psync.md) | Sent by a replica to its master to start or resume replication: PSYNC replication-id offset. | 1.1.0 |
| [`REPLCONF`](replconf.md) | Sent between a master and its replicas during replication: the replica's port, its acknowledged offset, and its capabilities. | 1.1.0 |
| [`REPLICAOF`](replicaof.md) | Makes the server a replica of the master at host port, or, with NO ONE, a master. | 1.1.0 |
| [`ROLE`](role.md) | Returns the server's replication role: master with its offset and replicas, or slave with its master and state. | 1.1.0 |
| [`SAVE`](save.md) | Writes a snapshot of the dataset to dump.kdb, in the working directory, before replying. | 1.1.0 |
| [`SELECT`](select.md) | Makes database index the connection's current one. | 1.1.0 |
| [`SHUTDOWN`](shutdown.md) | Stops the server, by default after saving a snapshot. | 1.1.0 |
| [`SLAVEOF`](slaveof.md) | Another name for REPLICAOF. | 1.1.0 |
| [`SYNC`](sync.md) | The original replication handshake: a replica sends it to get a snapshot, then every write. | 1.1.0 |
| [`TIME`](time.md) | Returns the server's clock: Unix seconds, and the microseconds within that second, as two bulk strings. | 1.1.0 |
| [`WAIT`](wait.md) | Waits until numreplicas replicas have acknowledged every write this connection made before it, or timeout milliseconds pass; 0 waits for ever. | 1.1.0 |
| [`WAITAOF`](waitaof.md) | Waits until every write this connection made before it is in the local AOF and fsynced (numlocal), and in numreplicas replicas' AOFs, or timeout milliseconds pass. | 1.1.0 |

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
| [`BZMPOP`](bzmpop.md) | ZMPOP that waits until one of the sorted sets has a member, or timeout seconds have passed. | 1.1.0 |
| [`BZPOPMAX`](bzpopmax.md) | BZPOPMIN for the highest score. | 1.1.0 |
| [`BZPOPMIN`](bzpopmin.md) | ZPOPMIN of one member from the first non-empty sorted set of those given. | 1.1.0 |
| [`ZADD`](zadd.md) | Adds members with scores to the sorted set at key, or updates the scores of members already in it. | 1.1.0 |
| [`ZCARD`](zcard.md) | Returns the number of members of the sorted set at key. | 1.1.0 |
| [`ZCOUNT`](zcount.md) | Counts the members of the sorted set at key with a score between min and max. | 1.1.0 |
| [`ZDIFF`](zdiff.md) | Returns the members of the first sorted set that are in none of the others, with their scores if WITHSCORES is given. | 1.1.0 |
| [`ZDIFFSTORE`](zdiffstore.md) | Stores what ZDIFF would return at destination, replacing whatever was there. | 1.1.0 |
| [`ZINCRBY`](zincrby.md) | Adds increment to the score of member in the sorted set at key. | 1.1.0 |
| [`ZINTER`](zinter.md) | Returns the members in every one of the given sorted sets, with scores combined. | 1.1.0 |
| [`ZINTERCARD`](zintercard.md) | Returns how many members the intersection of the given sorted sets has, without returning them. | 1.1.0 |
| [`ZINTERSTORE`](zinterstore.md) | Stores what ZINTER would return at destination, replacing whatever was there. | 1.1.0 |
| [`ZLEXCOUNT`](zlexcount.md) | Counts the members of the sorted set at key between min and max in lexicographical order. | 1.1.0 |
| [`ZMPOP`](zmpop.md) | Pops members from the first of the given sorted sets that is not empty: the lowest (MIN) or highest (MAX) scores, one or COUNT count of them. | 1.1.0 |
| [`ZMSCORE`](zmscore.md) | Returns the scores of several members of the sorted set at key. | 1.1.0 |
| [`ZPOPMAX`](zpopmax.md) | Removes and returns the members with the highest scores in the sorted set at key: one, or count. | 1.1.0 |
| [`ZPOPMIN`](zpopmin.md) | Removes and returns the members with the lowest scores in the sorted set at key: one, or count. | 1.1.0 |
| [`ZRANDMEMBER`](zrandmember.md) | Returns members of the sorted set at key, picked at random, without removing them. | 1.1.0 |
| [`ZRANGE`](zrange.md) | Returns members of the sorted set at key in a range. | 1.1.0 |
| [`ZRANGEBYLEX`](zrangebylex.md) | Returns members of the sorted set at key between min and max in lexicographical order, for sets whose members all have the same score. | 1.1.0 |
| [`ZRANGEBYSCORE`](zrangebyscore.md) | Returns members of the sorted set at key with scores from min to max, lowest first. | 1.1.0 |
| [`ZRANGESTORE`](zrangestore.md) | Stores the members ZRANGE would return, with their scores, at dst, replacing whatever was there. | 1.1.0 |
| [`ZRANK`](zrank.md) | Returns the rank of member in the sorted set at key: its position from the lowest score, starting at 0. | 1.1.0 |
| [`ZREM`](zrem.md) | Removes members from the sorted set at key. | 1.1.0 |
| [`ZREMRANGEBYLEX`](zremrangebylex.md) | Removes the members of the sorted set at key between min and max in lexicographical order, with bounds as ZRANGEBYLEX takes them. | 1.1.0 |
| [`ZREMRANGEBYRANK`](zremrangebyrank.md) | Removes the members of the sorted set at key with ranks from start to stop, both included. | 1.1.0 |
| [`ZREMRANGEBYSCORE`](zremrangebyscore.md) | Removes the members of the sorted set at key with scores from min to max. | 1.1.0 |
| [`ZREVRANGE`](zrevrange.md) | Returns members of the sorted set at key by rank, highest score first. | 1.1.0 |
| [`ZREVRANGEBYLEX`](zrevrangebylex.md) | ZRANGEBYLEX in reverse order; max comes first. | 1.1.0 |
| [`ZREVRANGEBYSCORE`](zrevrangebyscore.md) | Returns members of the sorted set at key with scores from max down to min. | 1.1.0 |
| [`ZREVRANK`](zrevrank.md) | Returns the rank of member from the highest score, starting at 0. | 1.1.0 |
| [`ZSCAN`](zscan.md) | Goes through the members of the sorted set at key a page at a time, as SCAN goes through keys. | 1.1.0 |
| [`ZSCORE`](zscore.md) | Returns the score of member in the sorted set at key. | 1.1.0 |
| [`ZUNION`](zunion.md) | Returns the members in any of the given sorted sets, with scores combined. | 1.1.0 |
| [`ZUNIONSTORE`](zunionstore.md) | Stores what ZUNION would return at destination, replacing whatever was there. | 1.1.0 |

## Stream

| Command | Summary | Since |
|---|---|---|
| [`XACK`](xack.md) | Acknowledges entries the group delivered: they are no longer pending. | 1.1.0 |
| [`XACKDEL`](xackdel.md) | Acknowledges entries for the group and deletes them from the stream, in one step (Redis 8.2). | 1.1.0 |
| [`XADD`](xadd.md) | Appends an entry, a set of field-value pairs, to the stream at key. | 1.1.0 |
| [`XAUTOCLAIM`](xautoclaim.md) | Goes through the group's pending entries from start and gives consumer those idle at least min-idle-time milliseconds, COUNT count at a time (100 by default). | 1.1.0 |
| [`XCFGSET`](xcfgset.md) | Sets the configuration of the stream at key. | 1.1.0 |
| [`XCLAIM`](xclaim.md) | Gives pending entries to consumer, if they have been idle at least min-idle-time milliseconds: for when the consumer that had them stopped. | 1.1.0 |
| [`XDEL`](xdel.md) | Deletes entries from the stream at key by ID. | 1.1.0 |
| [`XDELEX`](xdelex.md) | Deletes entries from the stream at key, with control over the references consumer groups hold to them (Redis 8.2). | 1.1.0 |
| [`XGROUP`](xgroup.md) | Creates and manages consumer groups: named readers of a stream that share its entries among their consumers, and track what each consumer has been given and not yet acknowledged. | 1.1.0 |
| [`XIDMPRECORD`](xidmprecord.md) | Records that producer producer-id's idempotent ID idempotent-id produced the entry id, already in the stream at key, as an XADD ... | 1.1.1 |
| [`XINFO`](xinfo.md) | Reports on a stream, its consumer groups and their consumers. | 1.1.0 |
| [`XLEN`](xlen.md) | Returns the number of entries in the stream at key. | 1.1.0 |
| [`XNACK`](xnack.md) | Releases pending entries back to the group without acknowledging them, so that another consumer can take them at once, with XREADGROUP ... | 1.1.0 |
| [`XPENDING`](xpending.md) | Returns the entries the group has delivered and that are not yet acknowledged. | 1.1.0 |
| [`XRANGE`](xrange.md) | Returns the entries of the stream at key with IDs from start to end, both included, oldest first. | 1.1.0 |
| [`XREAD`](xread.md) | Reads entries with IDs greater than the ones given, from one or more streams. | 1.1.0 |
| [`XREADGROUP`](xreadgroup.md) | Reads entries for consumer of consumer group group. | 1.1.0 |
| [`XREVRANGE`](xrevrange.md) | XRANGE, newest first; end comes first. | 1.1.0 |
| [`XSETID`](xsetid.md) | Sets the last ID of the stream at key, so that new entries get greater IDs. | 1.1.0 |
| [`XTRIM`](xtrim.md) | Removes the oldest entries of the stream at key. | 1.1.0 |

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
| [`TS.ADD`](ts.add.md) | Adds a sample to the time series at key: timestamp in milliseconds, or * for the server's clock, and value, a floating-point number or NaN. | 1.1.0 |
| [`TS.ALTER`](ts.alter.md) | Changes a time series' retention, chunk size, duplicate policy or labels. | 1.1.0 |
| [`TS.CREATE`](ts.create.md) | Creates a time series at key: samples, each a timestamp in milliseconds and a floating-point value, kept in timestamp order. | 1.1.0 |
| [`TS.CREATERULE`](ts.createrule.md) | Creates a compaction rule: every sample added to sourceKey is aggregated, by agg over buckets of bucketDuration milliseconds, into the existing series destKey. | 1.1.0 |
| [`TS.DECRBY`](ts.decrby.md) | TS.INCRBY, subtracting. | 1.1.0 |
| [`TS.DEL`](ts.del.md) | Deletes the samples of the time series at key from fromTimestamp to toTimestamp, both included. | 1.1.0 |
| [`TS.DELETERULE`](ts.deleterule.md) | Deletes the compaction rule from sourceKey to destKey. | 1.1.0 |
| [`TS.GET`](ts.get.md) | Returns the newest sample of the time series at key. | 1.1.0 |
| [`TS.INCRBY`](ts.incrby.md) | Adds a sample whose value is the series' last value plus value; a missing series starts at 0. | 1.1.0 |
| [`TS.INFO`](ts.info.md) | Returns a time series' metadata: its number of samples, memory use, first and last timestamps, retention, chunk size, duplicate policy, labels, and compaction rules. | 1.1.0 |
| [`TS.MADD`](ts.madd.md) | Adds samples to one or more time series in one call, creating series that do not exist. | 1.1.0 |
| [`TS.MGET`](ts.mget.md) | Returns the newest sample of every time series whose labels match the FILTER (see TS.MRANGE for conditions). | 1.1.0 |
| [`TS.MRANGE`](ts.mrange.md) | Runs TS.RANGE over every time series whose labels match the FILTER, and returns each with its samples. | 1.1.0 |
| [`TS.MREVRANGE`](ts.mrevrange.md) | TS.MRANGE, newest first, with the same options. | 1.1.0 |
| [`TS.NRANGE`](ts.nrange.md) | Runs the same range over several named time series and joins the results by timestamp, a command of Redis 8.10. | 1.1.0 |
| [`TS.NREVRANGE`](ts.nrevrange.md) | TS.NRANGE, newest first. | 1.1.0 |
| [`TS.QUERYINDEX`](ts.queryindex.md) | Returns the keys of every time series whose labels match the given conditions (see TS.MRANGE), sorted. | 1.1.0 |
| [`TS.QUERYLABELS`](ts.querylabels.md) | Returns the label names in use, with LABELS, or the values of one label, with VALUES label, across the time series that match the FILTER conditions, or all of them (Redis 8.10). | 1.1.0 |
| [`TS.RANGE`](ts.range.md) | Returns the samples of the time series at key from fromTimestamp to toTimestamp, both included, oldest first. | 1.1.0 |
| [`TS.READ`](ts.read.md) | Returns the samples of the time series at key at or after timestamp, oldest first, for following a series as it grows (Redis 8.10). | 1.1.0 |
| [`TS.REVRANGE`](ts.revrange.md) | TS.RANGE, newest first, with the same options. | 1.1.0 |

## Transaction

| Command | Summary | Since |
|---|---|---|
| [`DISCARD`](discard.md) | Drops the commands queued since MULTI, ends the transaction, and stops watching keys. | 1.1.0 |
| [`EXEC`](exec.md) | Runs the commands queued since MULTI, as one step: no other client's command that could see their keys starts between two of them, reads included, so nobody sees the transaction half done. | 1.1.0 |
| [`MULTI`](multi.md) | Starts a transaction on this connection. | 1.1.0 |
| [`UNWATCH`](unwatch.md) | Stops watching every key this connection watches. | 1.1.0 |
| [`WATCH`](watch.md) | Watches keys for the next transaction on this connection: if any of them is changed, by any client, before EXEC, the transaction runs nothing and EXEC replies nil. | 1.1.0 |

## Vector search

| Command | Summary | Since |
|---|---|---|
| [`FT.AGGREGATE`](ft.aggregate.md) | Runs a query and transforms its results: groups them, reduces each group, computes new fields, filters and sorts. | 1.1.0 |
| [`FT.ALIASADD`](ft.aliasadd.md) | Creates an alias for an index: a second name, usable wherever the index's name is. | 1.1.0 |
| [`FT.ALIASDEL`](ft.aliasdel.md) | Deletes an alias. | 1.1.0 |
| [`FT.ALIASLIST`](ft.aliaslist.md) | Returns the aliases that point to an index (Redis 8.10). | 1.1.0 |
| [`FT.ALIASUPDATE`](ft.aliasupdate.md) | Points an alias at an index, creating it if needed, or moving it from another index. | 1.1.0 |
| [`FT.ALTER`](ft.alter.md) | Adds fields to an index. | 1.1.0 |
| [`FT.CONFIG`](ft.config.md) | Reads and sets the search engine's settings, by RediSearch's names. | 1.1.0 |
| [`FT.CREATE`](ft.create.md) | Creates a search index over the hashes, or JSON documents, whose keys start with the given prefixes. | 1.1.0 |
| [`FT.CURSOR`](ft.cursor.md) | Reads and closes the cursors FT.AGGREGATE ... | 1.1.0 |
| [`FT.DEBUG`](ft.debug.md) | Maintenance of search indexes. | 1.1.0 |
| [`FT.DICTADD`](ft.dictadd.md) | Adds words to a dictionary: a named list of words, which FT.SPELLCHECK can include or exclude. | 1.1.0 |
| [`FT.DICTDEL`](ft.dictdel.md) | Removes words from a dictionary. | 1.1.0 |
| [`FT.DICTDUMP`](ft.dictdump.md) | Returns the words of a dictionary, sorted. | 1.1.0 |
| [`FT.DROPINDEX`](ft.dropindex.md) | Deletes an index. | 1.1.0 |
| [`FT.EXPLAIN`](ft.explain.md) | Returns how a query is understood, as Redis writes a query plan: INTERSECT { ... | 1.1.0 |
| [`FT.EXPLAINCLI`](ft.explaincli.md) | FT.EXPLAIN, as an array of its lines. | 1.1.0 |
| [`FT.HYBRID`](ft.hybrid.md) | Searches an index by text and by vector together, and fuses the two rankings into one. | 1.1.0 |
| [`FT.INFO`](ft.info.md) | Returns an index's definition and state: its key type and prefixes, its fields with their options, how many documents and terms it holds, and whether it is still indexing. | 1.1.0 |
| [`FT.PROFILE`](ft.profile.md) | Runs a query, SEARCH, AGGREGATE or HYBRID, and returns its result with a profile: total, parsing and lock-wait times, warnings, and the tree of iterators and result processors the query used. | 1.1.0 |
| [`FT.SEARCH`](ft.search.md) | Searches an index and returns the matching documents. | 1.1.0 |
| [`FT.SPELLCHECK`](ft.spellcheck.md) | Suggests spellings for the words of a query that are not in the index. | 1.1.0 |
| [`FT.SYNDUMP`](ft.syndump.md) | Returns an index's synonym groups, as each word followed by the groups it is in. | 1.1.0 |
| [`FT.SYNUPDATE`](ft.synupdate.md) | Creates or updates a synonym group of an index: words to be treated as the same. | 1.1.0 |
| [`FT.TAGVALS`](ft.tagvals.md) | Returns the distinct values of a TAG field across the indexed documents, sorted. | 1.1.0 |
| [`FT._LIST`](ft._list.md) | Returns the names of every index. | 1.1.0 |

## Vector set

| Command | Summary | Since |
|---|---|---|
| [`VADD`](vadd.md) | Adds an element with its vector to the vector set at key, or replaces an element's vector. | 1.1.0 |
| [`VCARD`](vcard.md) | Returns the number of elements of the vector set at key; 0 if it does not exist. | 1.1.0 |
| [`VDIM`](vdim.md) | Returns the number of dimensions of the vector set's vectors; nil if it does not exist. | 1.1.0 |
| [`VEMB`](vemb.md) | Returns an element's vector, as numbers; with RAW, as little-endian 32-bit floats. | 1.1.0 |
| [`VGETATTR`](vgetattr.md) | Returns an element's JSON attributes; nil if it has none. | 1.1.0 |
| [`VINFO`](vinfo.md) | Returns the vector set's dimensions, its number of elements, its quantization, its index type and its graph's levels. | 1.1.0 |
| [`VISMEMBER`](vismember.md) | Tells whether element is in the vector set at key: 1 or 0. | 1.1.0 |
| [`VLINKS`](vlinks.md) | Returns an element's nearest neighbours, up to 16, as one level; WITHSCORES gives their similarity. | 1.1.0 |
| [`VRANDMEMBER`](vrandmember.md) | Returns elements of the vector set at key, picked at random: one, or count different ones, or, with a negative count, exactly -count that may repeat. | 1.1.0 |
| [`VRANGE`](vrange.md) | Returns the elements of the vector set at key between two names in lexicographical order, with bounds as ZRANGEBYLEX takes them, and at most count. | 1.1.0 |
| [`VREM`](vrem.md) | Removes elements from the vector set at key. | 1.1.0 |
| [`VSETATTR`](vsetattr.md) | Sets an element's JSON attributes; an empty string removes them. | 1.1.0 |
| [`VSIM`](vsim.md) | Returns the elements of the vector set at key most similar to a vector, most similar first. | 1.1.0 |
