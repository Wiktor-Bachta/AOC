class Game:
    def __init__(self, line: str):
        words = line.split()
        self.id = words[1][:-1]
        self.winningNumbers = set()
        self.yourNumbers = set()
        i = 2
        while words[i] != "|":
            self.winningNumbers.add(int(words[i]))
            i += 1
        i += 1
        while i < len(words):
            self.yourNumbers.add(int(words[i]))
            i += 1

    def calculatePoints(self):
        matching = self.winningNumbers & self.yourNumbers
        if len(matching) == 0:
            return 0
        return 2 ** (len(matching) - 1)


if __name__ == "__main__":
    games = []

    with open("data.txt", "r") as data:
        for line in data:
            games.append(Game(line.rstrip()))

    result = 0

    for game in games:
        result += game.calculatePoints()

    print(result)
