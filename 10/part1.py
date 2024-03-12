pipes = {"|": [(-1, 0), (1, 0)], "-": [(0, -1), (0, 1)], "L": [(-1, 0), (0, 1)],
         "J": [(-1, 0), (0, -1)], "7": [(0, -1), (1, 0)], "F": [(0, 1), (1, 0)], ".": []}


def getNext(visited, pipeConnections):
    for pipeConnection in pipeConnections:
        if pipeConnection not in visited:
            visited.add(pipeConnection)
            return pipeConnection
    return (-1, -1)  # if whole loop is visited


if __name__ == "__main__":

    board = []

    with open("data.txt", "r") as data:
        for line in data:
            board.append([i for i in line.rstrip()])

    height = len(board)
    width = len(board[0])

    connections = [[[] for i in range(width)] for j in range(height)]

    for i in range(height):
        for j in range(width):
            symbol = board[i][j]
            if symbol == "S":
                startPosition = (i, j)
                continue
            for connection in pipes[symbol]:
                connectionY = i + connection[0]
                connectionX = j + connection[1]
                if (0 <= connectionY < height and 0 <= connectionX < width):
                    connections[i][j].append((connectionY, connectionX))

    steps = 0
    neighbours = []
    for i in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        neighbourY, neighbourX = startPosition[0] + \
            i[0], startPosition[1] + i[1]
        if (0 <= neighbourY < height and 0 <= neighbourX < width) and startPosition in connections[neighbourY][neighbourX]:
            neighbours.append((neighbourY, neighbourX))

    neighbour1 = neighbours[0]
    neighbour2 = neighbours[1]

    visited = {startPosition, neighbour1, neighbour2}

    while True:
        neighbour1 = getNext(
            visited, connections[neighbour1[0]][neighbour1[1]])
        neighbour2 = getNext(
            visited, connections[neighbour2[0]][neighbour2[1]])
        if neighbour1 == (-1, -1) or neighbour2 == (-1, -1):
            break

    result = len(visited) // 2

    print(result)
