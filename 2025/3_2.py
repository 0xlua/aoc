#!/usr/bin/env -S uv run

with open("input") as input:
    result = 0
    for bank in input.read().splitlines():
        total_bats = 12
        max_jols = [0] * total_bats
        index: int = -1
        for curr_bat in range(total_bats - 1, -1, -1):
            for i in range(index + 1, len(bank) - curr_bat):
                bat_jol: int = int(bank[i]) * pow(10, curr_bat)
                if bat_jol > max_jols[curr_bat]:
                    max_jols[curr_bat] = bat_jol
                    index = i
                    if max_jols[curr_bat] >= 9 * pow(10, curr_bat):
                        break
        result += sum(max_jols)

    print(result)
