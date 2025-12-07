#!/usr/bin/env -S uv run

with open("input") as input:
    result = 0
    data: list[str] = input.read().splitlines()
    ranges: list[list[int]] = sorted(
        [*map(lambda r: [*map(int, r.split("-"))], data[: data.index("")])]
    )
    curr: list[int] = ranges[0]
    for r in ranges[1:]:
        if r[0] <= curr[1] + 1:
            curr[1] = max(r[1], curr[1])
        else:
            result += curr[1] - curr[0] + 1
            curr = r
    result += curr[1] - curr[0] + 1

    print(result)
