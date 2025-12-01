with open("input.txt") as input:
    dial = 50
    result = 0
    for rot in input:
        dir = 1 if rot.startswith("R") else -1
        steps = int(rot[1:])
        dial = (dial + dir * steps) % 100
        if (dial == 0):
            result += 1
    print(result)
