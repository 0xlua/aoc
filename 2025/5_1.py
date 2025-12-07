#!/usr/bin/env -S uv run

with open("input") as input:
    result = 0
    lines = input.read().splitlines()
    divider = lines.index("")
    ranges = list(map(lambda r: list(map(int, r.split("-"))), lines[:divider]))
    ingrs = list(map(int, lines[divider + 1 :]))
    for ingr in ingrs:
        for range in ranges:
            if range[0] <= ingr <= range[1]:
                result += 1
                break
    print(result)
