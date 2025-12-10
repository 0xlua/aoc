#!/usr/bin/env -S uv run

from itertools import combinations


def area(rect):
    a, b = rect
    return (abs(a[1] - b[1]) + 1) * (abs(b[0] - a[0]) + 1)


with open("input") as input:
    tiles = [[*map(int, tile.split(","))] for tile in input.read().splitlines()]
    result = max(map(area, combinations(tiles, 2)))
    print(result)
