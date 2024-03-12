def transitionBackwards(seed: int, map) -> int:
    for mapRange in map:
        if mapRange["lowestDestination"] <= seed < mapRange["lowestDestination"] + mapRange["range"]:
            return mapRange["lowestSource"] + seed - mapRange["lowestDestination"]
    return seed


def transition(seed: int, map) -> int:
    for mapRange in map:
        if mapRange["lowestSource"] <= seed < mapRange["lowestSource"] + mapRange["range"]:
            return mapRange["lowestDestination"] + seed - mapRange["lowestSource"]
    return seed


def inAnySeedRange(i: int, seedRanges) -> bool:
    for seedRange in seedRanges:
        if seedRange["lowest"] <= i <= seedRange["highest"]:
            return True
    return False


if __name__ == "__main__":

    maps = []
    seeds = []
    bestLocation = 0

    with open("data.txt", "r") as data:
        lines = data.readlines()

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

    seedRanges = []
    seedInfo = [int(i) for i in lines[0].split()[1:]]
    for i in range(0, len(seedInfo), 2):
        seedRange = {}
        seedRange["lowest"] = int(seedInfo[i])
        seedRange["highest"] = seedRange["lowest"] + int(seedInfo[i + 1]) - 1
        seedRanges.append(seedRange)

    maps.reverse()

    candidates = [set() for i in range(len(maps) + 1)]
    for mapRange in maps[0]:
        candidates[0].add(mapRange["lowestDestination"])

    for i in range(1, len(maps)):
        for mapRange in maps[i]:
            candidates[i].add(mapRange["lowestDestination"])
            for candidate in candidates[i - 1]:
                candidates[i].add(
                    transitionBackwards(candidate, maps[i - 1]))

    for candidate in candidates[len(maps) - 1]:
        candidates[len(maps)].add(transitionBackwards(candidate, maps[-1]))

    possibleCandidates = []

    for candidate in set(candidates[-1]):
        if inAnySeedRange(candidate, seedRanges):
            possibleCandidates.append(candidate)

    translated = []
    maps.reverse()

    for candidate in possibleCandidates:
        t = candidate
        for map in maps:
            t = transition(t, map)
        translated.append(t)

    print(min(translated))
