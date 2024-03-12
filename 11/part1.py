def isEmptyRow(row: str) -> bool:
    for i in row:
        if i == "#":
            return False
    return True


def isEmptyColumn(board: list[list[str]], i: int) -> bool:
    for row in board:
        if row[i] == "#":
            return False
    return True


def getDistance(galaxy1: tuple, galaxy2: tuple) -> int:
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


if __name__ == "__main__":

    board = []

    with open("data.txt", "r") as data:
        for line in data:
            board.append([i for i in line.rstrip()])

    i = 0
    while i < len(board):
        if isEmptyRow(board[i]):
            board.insert(i, ["." for j in range(len(board[0]))])
            i += 1
        i += 1

    i = 0
    while i < len(board[0]):
        if isEmptyColumn(board, i):
            for row in board:
                row.insert(i, ".")
            i += 1
        i += 1

    galaxies = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "#":
                galaxies.append((i, j))

    result = 0
    for i in range(len(galaxies)):
        for j in range(i):
            result += getDistance(galaxies[i], galaxies[j])

    print(result)
