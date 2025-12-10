#!/usr/bin/env -S uv run

from math import hypot
from itertools import combinations, starmap
from functools import reduce
from operator import sub, mul


def diff(conn) -> int:
    # a, b = [map(int, c.split(",")) for c in conn]
    a, b = conn
    a = map(int, a.split(","))
    b = map(int, b.split(","))
    x = starmap(sub, zip(a, b))
    return int(hypot(*x))


with open("input") as input:
    coords: list[str] = input.read().splitlines()
    circuits: list[set[str]] = []
    for conn in map(set, sorted(combinations(coords, 2), key=diff)[:1000]):
        current = {*conn}
        old = []
        for c in circuits:
            if conn.isdisjoint(c):
                old.append(c)
            else:
                current.update(c)
        circuits = old + [current]

    result = reduce(mul, sorted(map(len, circuits), reverse=True)[:3])
    print(result)
