with open("input") as input:
    result = 0
    # read all id ranges
    for r in input.read().split(","):
        # parse the start and end id
        start, end = r.split("-")
        # generate all ids in a range
        for id in range(int(start), int(end)):
            id_str = str(id)
            leng = len(id_str)
            if id_str[0:leng//2] == id_str[leng//2:]:
                result += id
    print(result)
