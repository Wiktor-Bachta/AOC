import math


def checkEnd(nodes) -> bool:
    for node in nodes:
        if node[-1] != "Z":
            return False
    return True


if __name__ == "__main__":

    nodes = {}

    with open("data.txt", "r") as data:
        lines = data.readlines()

    instructions = lines[0].rstrip()

    for i in range(2, len(lines)):
        words = lines[i].split()
        node = {}
        node["L"] = words[2][1:4]
        node["R"] = words[3][:3]
        nodes[words[0]] = node

        startingNodes = [node for node in nodes if node[-1] == "A"]

    stepCounts = []

    for startingNode in startingNodes:
        steps = 0
        currentNode = startingNode
        while True:
            instruction = instructions[steps % len(instructions)]
            currentNode = nodes[currentNode][instruction]
            steps += 1
            if (currentNode[-1] == "Z"):
                stepCounts.append(steps)
                break

    result = math.lcm(*stepCounts)
    print(result)
