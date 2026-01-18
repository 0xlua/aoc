#!/usr/bin/env -S uv run


def parse_input(lines: list[str]) -> dict[str, list[str]]:
    return {dev[0]: dev[-1].split(" ") for dev in [line.split(": ") for line in lines]}


def find_paths(
    paths: list[list[str]], devices: dict[str, list[str]]
) -> list[list[str]]:
    new_paths: list[list[str]] = [path for path in paths if path[-1] == "out"]
    for path in paths:
        if path[-1] == "out":
            continue
        for output in devices[path[-1]]:
            new_paths.append(path + [output])
    if all(path[-1] == "out" for path in paths):
        return paths
    else:
        return find_paths(new_paths, devices)


with open("input") as input:
    devices = parse_input(input.read().splitlines())
    paths = find_paths([["svr"]], devices)
    result = len([path for path in paths if "dac" in path and "fft" in path])
    print(result)
