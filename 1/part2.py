numbers = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "one": 1,
           "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
lengths = [len(value) for value in numbers]


def getFirst(line: str) -> int:
    i = 0
    while True:
        for length in lengths:
            word = line[i: i + length]
            if word in numbers:
                return numbers[word]
        i += 1


def getLast(line: str) -> int:
    j = len(line) - 1
    while True:
        for length in lengths:
            word = line[j: j + length]
            if word in numbers:
                return numbers[word]
        j -= 1


def getValue(line: str) -> int:
    return 10 * getFirst(line) + getLast(line)


if __name__ == "__main__":

    result = 0

    with open("data.txt", "r") as data:
        for line in data:
            result += getValue(line)

    print(result)
