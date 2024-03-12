pipes = {"|": [(-1, 0), (1, 0)], "-": [(0, -1), (0, 1)], "L": [(-1, 0), (0, 1)],
         "J": [(-1, 0), (0, -1)], "7": [(1, 0), (0, -1)], "F": [(1, 0), (0, 1)], ".": []}


def getInLoop(row: list[str]) -> int:
    important = {"|", "L", "J", "7", "F"}
    landmarks = []
    for i in range(len(row)):
        if row[i] in important:
            landmarks.append((row[i], i))

    intervals = []
    for i in range(len(landmarks)):
        if landmarks[i][0] == "|":
            intervals.append(
                {"start": landmarks[i][1], "end": landmarks[i][1], "flip": True})
        elif (landmarks[i][0] == "L" and landmarks[i + 1][0] == "7") or (landmarks[i][0] == "F" and landmarks[i + 1][0] == "J"):
            intervals.append(
                {"start": landmarks[i][1], "end": landmarks[i + 1][1], "flip": True})
        elif (landmarks[i][0] == "L" and landmarks[i + 1][0] == "J") or (landmarks[i][0] == "F" and landmarks[i + 1][0] == "7"):
            intervals.append(
                {"start": landmarks[i][1], "end": landmarks[i + 1][1], "flip": False})

    result = 0
    inside = False
    for i in range(len(intervals) - 1):
        inside = (inside != intervals[i]["flip"])
        if inside:
            result += intervals[i + 1]["start"] - intervals[i]["end"] - 1
    return result


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
    relativeNeighbours = []
    for i in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        neighbourY, neighbourX = startPosition[0] + \
            i[0], startPosition[1] + i[1]
        if (0 <= neighbourY < height and 0 <= neighbourX < width) and startPosition in connections[neighbourY][neighbourX]:
            neighbours.append((neighbourY, neighbourX))
            relativeNeighbours.append(i)

    for pipe, relNeighbours in pipes.items():
        if relNeighbours == relativeNeighbours:
            board[startPosition[0]][startPosition[1]] = pipe
            break

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

    for i in range(height):
        for j in range(width):
            if (i, j) not in visited:
                board[i][j] = "."
                
    result = 0

    for row in board:
        result += getInLoop(row)

    print(result)
