#!/usr/bin/env -S uv run

with open("input") as input:
    dial = 50
    result = 0
    for rot in input:
        dir = 1 if rot.startswith("R") else -1
        steps = int(rot[1:])
        for _ in range(steps):
            dial = (dial + dir) % 100
            if dial == 0:
                result += 1

    print(result)
