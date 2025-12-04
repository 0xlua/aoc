#!/usr/bin/env -S uv run


def accessible(x: int, y: int, grid: list[str]) -> bool:
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
        return adj_rolls < 4
    else:
        return False


def print_grid(grid: list[str]):
    for row in grid:
        print(row)


with open("input") as input:
    result = 0
    grid: list[str] = input.read().splitlines()
    size = len(grid)
    while True:
        old_grid = grid.copy()
        for y in range(size):
            new_line = old_grid[y]
            for x in range(size):
                if accessible(x, y, old_grid):
                    new_line = f"{new_line[:x]}.{new_line[x + 1 :]}"
                    result += 1
            grid[y] = new_line
        if grid == old_grid:
            break

    print(result)
