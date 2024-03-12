def transition(seed: int, map) -> int:
    for mapRange in map:
        if mapRange["lowestSource"] <= seed < mapRange["lowestSource"] + mapRange["range"]:
            return mapRange["lowestDestination"] + seed - mapRange["lowestSource"]
    return seed


if __name__ == "__main__":

    maps = []

    with open("data.txt", "r") as data:
        lines = data.readlines()

    seeds = [int(i) for i in lines[0].split()[1:]]

    mapNumber = 0
    i = 3
    while i < len(lines):
        map = []
        while i < len(lines) and lines[i] != "\n":
            mapRange = {}
            info = lines[i].split()
            mapRange["lowestDestination"] = int(info[0])
            mapRange["lowestSource"] = int(info[1])
            mapRange["range"] = int(info[2])
            map.append(mapRange)
            i += 1
        maps.append(map)
        i += 2

    for map in maps:
        for i in range(len(seeds)):
            seeds[i] = transition(seeds[i], map)

    print(min(seeds))
