cardVals = {"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8, "9": 7,
            "8": 6, "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0}


def handToValue(hand: str) -> tuple:

    content = {}

    for card in hand:
        if card not in content:
            content[card] = 1
        else:
            content[card] += 1

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
