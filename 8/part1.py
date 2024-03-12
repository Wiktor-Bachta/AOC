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

    currentNode = "AAA"
    i = 0
    while currentNode != "ZZZ":
        instruction = instructions[i % len(instructions)]
        currentNode = nodes[currentNode][instruction]
        i += 1

    print(i)
