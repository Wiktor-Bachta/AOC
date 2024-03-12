class Game:
    def __init__(self, line: str):
        words = line.split()
        self.id = int(words[1][:-1])
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

        wonAmount = len(self.winningNumbers & self.yourNumbers)
        self.wonScratchcards = [self.id + i for i in range(1, wonAmount + 1)]


if __name__ == "__main__":
    games = []

    with open("data.txt", "r") as data:
        for line in data:
            games.append(Game(line.rstrip()))

    numCards = [1 for i in range(len(games))]

    for i in range(1, len(numCards)):
        for j in range(i):
            if (i + 1) in games[j].wonScratchcards:
                numCards[i] += numCards[j]

    result = sum(numCards)

    print(result)
