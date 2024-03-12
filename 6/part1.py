def getNumberOfWays(time: int, distance: int) -> int:
    chargingTime = 1
    while chargingTime * (time - chargingTime) <= distance:
        chargingTime += 1
    return time + 1 - 2 * chargingTime


if __name__ == "__main__":

    races = []
    result = 1

    with open("data.txt", "r") as data:
        times = data.readline().split()[1:]
        distances = data.readline().split()[1:]

    for i in range(len(times)):
        races.append({"time": int(times[i]), "distance": int(distances[i])})

    for race in races:
        result *= getNumberOfWays(race["time"], race["distance"])

    print(result)
