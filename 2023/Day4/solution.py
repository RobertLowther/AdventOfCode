class Card:
    targetNumbers = []
    scratchNumbers = []
    matches = 0

    def __init__(self, tNums, sNums):
        self.targetNumbers = tNums
        self.scratchNumbers = sNums

        for sNum in sNums:
            if sNum in tNums: self.matches += 1

inFile = open("2023/Day4\\data.txt")
data = inFile.readlines()
inFile.close()

cards = []
cardsDict = {}

for i in range(len(data)):
    line = data[i].strip()
    cardData = line.split(":")[1].strip()
    targetNumbers, scratchNumbers = ([int(y) for y in x.strip().split()] for x in cardData.split("|"))
    cards.append(Card(targetNumbers, scratchNumbers))

    if cards[-1] in cardsDict:
        cardsDict[cards[-1]] += 1
    else:
        cardsDict[cards[-1]] = 1

for i in range(len(cards)):
    for j in range(1, cards[i].matches + 1):
        cardsDict[cards[i + j]] += cardsDict[cards[i]]

total = 0

for val in cardsDict.values():
    total += val

print(total)