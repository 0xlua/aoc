#!/usr/bin/env -S uv run

with open("input") as input:
    result = 0
    grid: list[str] = input.read().splitlines()
    size = len(grid)
    for y in range(size):
        for x in range(size):
            adj_rolls = 0
            if grid[y][x] == "@":
                for adj_y in range(y - 1, y + 2):
                    if adj_y >= 0 and adj_y < size:
                        for adj_x in range(x - 1, x + 2):
                            if (
                                adj_x >= 0
                                and adj_x < size
                                and (x != adj_x or y != adj_y)
                                and grid[adj_y][adj_x] == "@"
                            ):
                                adj_rolls += 1
                if adj_rolls < 4:
                    result += 1
    print(result)
