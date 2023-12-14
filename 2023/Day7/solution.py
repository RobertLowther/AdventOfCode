from functools import cmp_to_key

class Hand:
    HAND_RANKS = {
        0: "High Card",
        1: "One Pair",
        2: "Two Pair",
        3: "Three of a kind",
        4: "Full house",
        5: "Four of a Kind",
        6: "Five of a Kind",
    }


    CARD_VALUES = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'T',
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A',
    }


    def __init__(self, hand: str, bid: int, wildJ = False):
        self.hand = hand
        self.bid = int(bid)
        self.rank = Hand.determineRank(self.hand, wildJ)

    
    def __repr__(self) -> str:
        return repr((self.hand, self.bid, self.rank))


    def determineRank(hand: str, wildJ = False):
        cardLabels = {}

        for i in hand:
            cardLabels[i] = cardLabels[i] + 1 if i in cardLabels.keys() else 1

        if wildJ and 'J' in cardLabels and hand != "JJJJJ":
            maxCount = []
            for label in cardLabels.keys():
                if label == 'J': continue

                if len(maxCount) == 0:
                    maxCount.append(label)
                else:
                    if cardLabels[label] > cardLabels[maxCount[0]]: maxCount = [label]
                    elif cardLabels[label] == cardLabels[maxCount[0]]: maxCount.append(label)

            maxVal = ''

            for label in maxCount:
                if maxVal == '':
                    maxVal = label
                else:
                    if Hand.CARD_VALUES[label] > Hand.CARD_VALUES[maxVal]:
                        maxVal = label

            cardLabels[maxVal] += cardLabels['J']
            del cardLabels['J']

        rank = 0
        uniqueCardCount = len(cardLabels.keys())

        if uniqueCardCount == 1: # Five of a kind
            rank = 6
        elif uniqueCardCount == 2: # Four of a kind or full house
            sampleIndex = 0
            sampleLabel = hand[sampleIndex]

            while sampleLabel == "J":
                sampleIndex += 1
                sampleLabel = hand[sampleIndex]

            if cardLabels[sampleLabel] == 1 or cardLabels[sampleLabel] == 4: # Four of a kind
                rank = 5
            else: # Full house
                rank = 4
        elif uniqueCardCount == 3: # Three of a kind or Two Pair
            for i in cardLabels.keys():
                if cardLabels[i] == 3: # Three of a kind
                    rank = 3
                    break
                elif cardLabels[i] == 2: # Two Pair
                    rank = 2
                    break
        elif uniqueCardCount == 4:
            rank = 1
        else:
            rank = 0

        return rank
    

    def Compare(hand1: 'Hand', hand2: 'Hand'):
        if hand1.rank == hand2.rank:
            for i in range(len(hand1.hand) if len(hand1.hand) < len(hand2.hand) else len(hand2.hand)):
                if Hand.CARD_VALUES[hand1.hand[i]] < Hand.CARD_VALUES[hand2.hand[i]]:
                    return -1
                elif Hand.CARD_VALUES[hand1.hand[i]] > Hand.CARD_VALUES[hand2.hand[i]]:
                    return 1
            return -1 if len(hand1.hand) < len(hand2.hand) else 1
        elif hand1.rank < hand2.rank:
            return -1
        else:
            return 1


def GetHands(wildJ = False):
    data = []
    with open("2023/Day7/data.txt", "r") as inFile:
        data = [[value for value in line.strip().split()] for line in inFile.readlines()]

    hands = []

    for hand in data:
        hands.append(Hand(hand[0], hand[1], wildJ))

    return hands


def Solution1() -> int:
    hands = sorted(GetHands(), key=cmp_to_key(Hand.Compare))

    result = 0

    for i in range(len(hands)):
        result += hands[i].bid * (i + 1)

    return result


def Solution2() -> int:
    Hand.CARD_VALUES['J'] = 1
    hands = sorted(GetHands(True), key=cmp_to_key(Hand.Compare))

    result = 0

    for i in range(len(hands)):
        result += hands[i].bid * (i + 1)

    return result


print(Solution1())
print(Solution2())