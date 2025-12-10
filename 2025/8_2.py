#!/usr/bin/env -S uv run

from math import hypot
from itertools import combinations, starmap
from operator import sub, mul


def diff(conn) -> int:
    # a, b = [map(int, c.split(",")) for c in conn]
    a, b = conn
    a = map(int, a.split(","))
    b = map(int, b.split(","))
    x = starmap(sub, zip(a, b))
    return int(hypot(*x))


def connect(conn, circuits):
    old = []
    for c in circuits:
        if conn.isdisjoint(c):
            old.append(c)
        else:
            conn.update(c)
    return old + [conn]


with open("input") as input:
    coords: list[str] = input.read().splitlines()
    connections = [*map(set, sorted(combinations(coords, 2), key=diff))]
    circuits: list[set[str]] = [{c} for c in coords]
    for conn in connections[:1000]:
        circuits = connect(conn.copy(), circuits)
    for conn in connections[1000:]:
        circuits = connect(conn.copy(), circuits)
        if len(circuits) == 1:
            print(mul(*[int(c.split(",")[0]) for c in conn]))
            break
