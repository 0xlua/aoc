#!/usr/bin/env -S uv run

from itertools import combinations


def parse_lights(lights: str) -> list[bool]:
    return [bool(light == "#") for light in lights]


def parse_buttons(buttons: list[str]) -> list[list[int]]:
    return [[*map(int, button[1:-1].split(","))] for button in buttons]


def parse_line(line: list[str]):
    lights = parse_lights(line[0][1:-1])
    buttons = parse_buttons(line[1:-1])
    return lights, buttons


def parse_lines(lines: list[str]):
    return [parse_line(line.split(" ")) for line in lines]


def press_buttons(btn_seq: list[list[int]], machine_len) -> list[bool]:
    machine: list[bool] = [False] * machine_len
    for btn in btn_seq:
        for light in btn:
            machine[light] = not machine[light]
    return machine


with open("input") as input:
    result = 0
    for lights, buttons in parse_lines(input.read().splitlines()):
        presses = 1
        while True:
            for btn_seq in [[*c] for c in combinations(buttons, presses)]:
                machine: list[bool] = press_buttons(btn_seq, len(lights))
                if machine == lights:
                    result += presses
                    break
            else:
                presses += 1
                continue
            break
    print(result)
