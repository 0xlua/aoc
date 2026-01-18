#!/usr/bin/env -S uv run

with open("input") as input:
    result = 0
    lines: list[str] = input.read().splitlines()
    indeces: set[int] = {lines[0].index("S")}
    for line in lines[1:]:
        new_indeces: set[int] = set()
        for i in indeces:
            if line[i] == "^":
                result += 1
                new_indeces |= {i - 1, i + 1}
            else:
                new_indeces.add(i)
        indeces = new_indeces

    print(result)
