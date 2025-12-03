#!/usr/bin/env -S uv run

with open("input") as input:
    result = 0
    for bank in input.read().splitlines():
        first_max_jol: int = 0
        index: int = 0
        for i in range(len(bank) - 1):
            bat_jol: int = int(bank[i])
            if bat_jol > first_max_jol:
                first_max_jol = bat_jol
                index = i
                if first_max_jol >= 9:
                    break
        second_max_jol = 0
        for i in range(index + 1, len(bank)):
            bat_jol: int = int(bank[i])
            if bat_jol > second_max_jol:
                second_max_jol = bat_jol
                if second_max_jol >= 9:
                    break
        result += first_max_jol * 10 + second_max_jol

    print(result)
