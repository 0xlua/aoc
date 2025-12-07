#!/usr/bin/env -S uv run

from math import prod
import re

with open("input") as input:
    result = 0
    problems: list[str] = input.read().splitlines()
    symbols: list[str] = re.findall(r"[\+\*]\s+", problems[-1])
    for i in range(len(symbols)):
        symbol: str = symbols[i][:-1] if i < len(symbols) - 1 else symbols[i]
        index: int = sum(map(len, symbols[:i]))
        digits: list[str] = [p[index : index + len(symbol)] for p in problems[:-1]]
        converted_digits: list[int] = [
            int("".join([d[i] for d in digits])) for i in range(len(symbol))
        ]
        result += (
            sum(converted_digits) if symbol.startswith("+") else prod(converted_digits)
        )
    print(result)
