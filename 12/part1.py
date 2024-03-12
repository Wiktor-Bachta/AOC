def isInvalid(puzzle: dict) -> bool:

    schema = "".join(puzzle["schema"]).split(".")
    schema = [i for i in schema if i != ""]
    for i in range(len(schema)):
        schema[i] = [i for i in schema[i]]

    full = []
    i = 0
    while i < len(schema) and "?" not in schema[i]:
        full.append(schema[i])
        i += 1

    for i in range(len(full)):
        if i >= len(puzzle["intervals"]):
            return True
        if len(full[i]) != puzzle["intervals"][i]:
            return True

    if len(full) == len(schema):
        if len(full) == len(puzzle["intervals"]):
            return False
        else:
            return True
    return False


def getCombinations(puzzle: dict) -> int:

    if isInvalid(puzzle):
        return 0

    if "?" not in puzzle["schema"]:
        if isInvalid(puzzle):
            return 0
        else:
            return 1

    result = 0
    index = puzzle["schema"].index("?")
    puzzle["schema"][index] = "."
    result += getCombinations(puzzle)
    puzzle["schema"][index] = "#"
    result += getCombinations(puzzle)
    puzzle["schema"][index] = "?"
    return result


if __name__ == "__main__":

    puzzles = []

    with open("data.txt", "r") as data:
        for line in data:
            puzzle = {}
            line = line.split()
            line[1] = line[1].split(",")
            puzzle["schema"] = [i for i in line[0]]
            puzzle["intervals"] = [int(i) for i in line[1]]
            puzzles.append(puzzle)

    result = 0

    for puzzle in puzzles:
        result += getCombinations(puzzle)

    print(result)
