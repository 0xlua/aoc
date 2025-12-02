with open("input") as input:
    result = 0
    # read all id ranges
    for r in input.read().split(","):
        # parse the start and end id
        start, end = r.split("-")
        # generate all ids in a range
        for id in range(int(start), int(end)):
            # get all dividors of the id length
            leng = len(str(id)) # number of digits in id
            for d in range(1, leng // 2 + 1):
                if leng % d == 0: # only if d is actually a dividor
                    id_str = str(id)
                    substrings = [id_str[i:i+d] for i in range(0, len(id_str), d)] #
                    if len(set(substrings)) == 1: # check if all substrings of the id are equal
                        result += id
                        break
    print(result)
