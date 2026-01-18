#!/usr/bin/env -S uv run

from itertools import combinations, product


def parse_lights(lights: str) -> list[bool]:
    return [bool(light == "#") for light in lights]


def parse_buttons(buttons: list[str]) -> list[list[int]]:
    return [[*map(int, button[1:-1].split(","))] for button in buttons]


def parse_joltages(joltage: str) -> list[int]:
    return [*map(int, joltage.split(","))]


def parse_line(line: list[str]):
    lights = parse_lights(line[0][1:-1])
    buttons = parse_buttons(line[1:-1])
    joltages = parse_joltages(line[-1][1:-1])
    return lights, buttons, joltages


def parse_lines(lines: list[str]):
    return [parse_line(line.split(" ")) for line in lines]


def press_buttons(btn_seq: list[list[int]], machine_goal: list[int]) -> list[int]:
    machine: list[int] = [0] * len(machine_goal)
    for btn in btn_seq:
        for light in btn:
            machine[light] += 1
            if machine[light] > machine_goal[light]:
                return machine
    return machine


with open("input10.bsp") as input:
    result = 0
    for _, buttons, joltages in [parse_lines(input.read().splitlines())[0]]:
        print(joltages)
        presses = 10
        while True:
            for btn_seq in [[*c] for c in combinations(buttons, presses)]:
                machine: list[int] = press_buttons(btn_seq, joltages)
                print(btn_seq)
                print(machine)
                print("")
                if machine == joltages:
                    result += presses
                    break
            else:
                presses += 1
                continue
            break
    print(result)
