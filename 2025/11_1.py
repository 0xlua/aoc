#!/usr/bin/env -S uv run


def parse_input(lines: list[str]) -> dict[str, list[str]]:
    return {dev[0]: dev[-1].split(" ") for dev in [line.split(": ") for line in lines]}


def find_paths(outputs: list[str], devices: dict[str, list[str]]) -> int:
    if outputs[0] == "out":
        return 1
    counter = 0
    for output in outputs:
        counter += find_paths(devices[output], devices)
    return counter


with open("input") as input:
    devices = parse_input(input.read().splitlines())
    result = find_paths(devices["you"], devices)
    print(result)
