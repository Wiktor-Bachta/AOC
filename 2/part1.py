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

    def isValid(self, allowedMaximums: dict) -> bool:
        for color in allowedMaximums:
            if self.maximums[color] > allowedMaximums[color]:
                return False
        return True


if __name__ == "__main__":
    games = []
    allowedMaximums = {"red": 12, "green": 13, "blue": 14}
    result = 0

    with open("data.txt", "r") as data:
        for line in data:
            games.append(Game(line))

    for game in games:
        if game.isValid(allowedMaximums):
            result += game.id

    print(result)
