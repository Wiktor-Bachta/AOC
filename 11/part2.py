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


def getDistance(galaxy1: tuple, galaxy2: tuple, empyRowIndexes: list[int], emptyColumIndexes: list[int]) -> int:

    lowY = min(galaxy1[0], galaxy2[0])
    highY = max(galaxy1[0], galaxy2[0])
    lowX = min(galaxy1[1], galaxy2[1])
    highX = max(galaxy1[1], galaxy2[1])

    pasedEmptyRows = 0
    passedEmptyColumns = 0
    for i in empyRowIndexes:
        if lowY < i < highY:
            pasedEmptyRows += 1
    for i in emptyColumIndexes:
        if lowX < i < highX:
            passedEmptyColumns += 1

    return highX - lowX + highY - lowY + (1000000 - 1) * (passedEmptyColumns + pasedEmptyRows)


if __name__ == "__main__":

    board = []

    with open("data.txt", "r") as data:
        for line in data:
            board.append([i for i in line.rstrip()])

    empyRowIndexes = []
    emptyColumIndexes = []

    for i in range(len(board)):
        if isEmptyRow(board[i]):
            empyRowIndexes.append(i)

    for i in range(len(board[0])):
        if isEmptyColumn(board, i):
            emptyColumIndexes.append(i)

    galaxies = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "#":
                galaxies.append((i, j))

    result = 0
    for i in range(len(galaxies)):
        for j in range(i):
            result += getDistance(galaxies[i], galaxies[j],
                                  empyRowIndexes, emptyColumIndexes)

    print(result)
