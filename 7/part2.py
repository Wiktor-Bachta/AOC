cardVals = {"A": 12, "K": 11, "Q": 10, "J": 0, "T": 9, "9": 8,
            "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}


def handToValue(hand: str) -> tuple:

    if hand == "JJJJJ":
        return (6, 0, 0, 0, 0, 0)

    handNoJacks = [card for card in hand if card != "J"]
    numJacks = hand.count("J")
    content = {}

    for card in handNoJacks:
        if card not in content:
            content[card] = 1
        else:
            content[card] += 1

    mostFrequentCards = [card for card, frequency in content.items(
    ) if frequency == max(content.values())]
    for i in range(numJacks):
        content[mostFrequentCards[0]] += 1

    different = len(content)

    if different == 1:
        priority = 6
    elif different == 2 and (4 in content.values()):
        priority = 5
    elif different == 2:
        priority = 4
    elif different == 3 and (3 in content.values()):
        priority = 3
    elif different == 3:
        priority = 2
    elif different == 4:
        priority = 1
    else:
        priority = 0

    score = [priority]
    for card in hand:
        score.append(cardVals[card])

    return tuple(score)


if __name__ == "__main__":

    hands = []
    result = 0

    with open("data.txt", "r") as data:
        for line in data:
            line = line.split()
            hands.append({"cards": line[0], "bid": int(line[1])})

    for hand in hands:
        hand["score"] = handToValue(hand["cards"])

    # sorts by score increasing
    hands = sorted(hands, key=lambda d: d["score"])

    for i in range(len(hands)):
        result += (i + 1) * hands[i]["bid"]

    print(result)
