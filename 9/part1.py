def isOnlyZeros(a: list[int]) -> bool:
    for i in a:
        if i != 0:
            return False
    return True


def getDifference(a: list[int]) -> list[int]:
    difference = []
    for i in range(1, len(a)):
        difference.append(a[i] - a[i - 1])
    return difference


def getNext(sequence: list[int]) -> int:
    steps = [sequence]
    result = 0

    while True:
        if isOnlyZeros(steps[-1]):
            break
        steps.append(getDifference(steps[-1]))

    for step in steps:
        result += step[-1]

    return result


if __name__ == "__main__":

    result = 0
    sequences = []

    with open("data.txt", "r") as data:
        for line in data:
            input = line.split()
            sequences.append([int(i) for i in input])

    for sequence in sequences:
        result += getNext(sequence)

    print(result)
