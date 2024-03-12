def getValue(line: str) -> int:

    i = 0
    j = len(line) - 1

    while not line[i].isdigit():
        i += 1
    while not line[j].isdigit():
        j -= 1

    return 10 * int(line[i]) + int(line[j])


if __name__ == "__main__":

    result = 0

    with open("data.txt", "r") as data:
        for line in data:
            result += getValue(line)

    print(result)
