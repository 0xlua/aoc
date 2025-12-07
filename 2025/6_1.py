#!/usr/bin/env -S uv run

from math import prod

with open("input") as input:
    result = 0
    problems: list[list[str]] = [line.split() for line in input.read().splitlines()]
    for i in range(len(problems[0])):
        op: str = problems[-1][i]
        digits: list[int] = [int(p[i]) for p in problems[:-1]]
        result += sum(digits) if op == "+" else prod(digits)
    print(result)
