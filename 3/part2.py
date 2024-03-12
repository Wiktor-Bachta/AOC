def calculateFullNumber(board: list, height: int, width: int, y: int, x: int) -> int:
    number = [board[y][x]]
    board[y][x] = "."
    i = x - 1
    while i >= 0 and board[y][i].isdigit():
        number.insert(0, board[y][i])
        board[y][i] = "."
        i -= 1
    i = x + 1
    while i < width and board[y][i].isdigit():
        number.append(board[y][i])
        board[y][i] = "."
        i += 1
    number = int("".join(number))
    return number


def checkNeighbours(board: list, height: int, width: int, y: int, x: int) -> int:
    neighbourProduct = 1
    numNeighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (0 <= y + i < height and 0 <= x + j < width) and (i != 0 or j != 0):
                if (board[y + i][x + j].isdigit()):
                    neighbourProduct *= calculateFullNumber(board,
                                                  height, width, y + i, x + j)
                    numNeighbours += 1
    if numNeighbours < 2:
        return 0
    return neighbourProduct


if __name__ == "__main__":
    board = []
    with open("data.txt", "r") as data:
        for line in data:
            board.append(list(line.rstrip()))

    height = len(board)
    width = len(board[0])
    result = 0

    for y in range(height):
        for x in range(width):
            if board[y][x] == "*":
                result += checkNeighbours(board, height, width, y, x)

    print(result)
