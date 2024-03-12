class Game:
    def __init__(self, line: str):
        toDelete = {":", ",", ";", "\n"}
        for expression in toDelete:
            line = line.replace(expression, "")
        words = line.split(" ")

        self.id = int(words[1])
        self.maximums = {"red": 0, "green": 0, "blue": 0}

        for i in range(3, len(words), 2):
            self.maximums[words[i]] = max(
                self.maximums[words[i]], int(words[i - 1]))


if __name__ == "__main__":
    games = []
    result = 0

    with open("data.txt", "r") as data:
        for line in data:
            games.append(Game(line))

    for game in games:
        power = 1
        for amount in game.maximums.values():
            power *= amount
        result += power

    print(result)
