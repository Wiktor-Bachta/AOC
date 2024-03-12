def getNumberOfWays(time: int, distance: int) -> int:
    chargingTime = 1
    while chargingTime * (time - chargingTime) <= distance:
        chargingTime += 1
    return time + 1 - 2 * chargingTime


if __name__ == "__main__":

    races = []

    with open("data.txt", "r") as data:
        time = int("".join(data.readline().split()[1:]))
        distance = int("".join(data.readline().split()[1:]))

    result = getNumberOfWays(time, distance)
    print(result)
