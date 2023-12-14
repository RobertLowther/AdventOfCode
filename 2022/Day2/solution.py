LOSS = "loss"
TIE = "tie"
WIN = "win"


KEY_MAPPING = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}


SHAPE_VALUES = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


OUTCOME_VALUES = {
    LOSS: 0,
    TIE: 3,
    WIN: 6,
}


WINNING_MATCHUPS = {
    'X': 'Z',
    'Y': 'X',
    'Z': 'Y',
    'A': 'C',
    'B': 'A',
    'C': 'B',
}


LOSING_MATCHUPS = {
    'X': 'Y',
    'Y': 'Z',
    'Z': 'X',
    'A': 'B',
    'B': 'C',
    'C': 'A',
}


def PlayRound(opponentChoice: str, playerChoice: str):
    # Ensure that all shapes are in the form of X, Y, or Z
    if opponentChoice in "ABC": opponentChoice = KEY_MAPPING[opponentChoice]
    if playerChoice in "ABC": playerChoice = KEY_MAPPING[playerChoice]

    score = SHAPE_VALUES[playerChoice]

    if opponentChoice == playerChoice:
        score += OUTCOME_VALUES[TIE]
    elif opponentChoice == WINNING_MATCHUPS[playerChoice]:
        score += OUTCOME_VALUES[WIN]
    elif opponentChoice == LOSING_MATCHUPS[playerChoice]:
        score += OUTCOME_VALUES[LOSS]
    
    return score

def Solution1(data: list[str]):

    rounds = ([[shape for shape in line.strip().split()] for line in data])

    finalScore = 0

    for round in rounds:
        finalScore += PlayRound(round[0], round[1])

    print(finalScore)

def Solution2(data: list[str]):

    rounds = ([[shape for shape in line.strip().split()] for line in data])

    finalScore = 0

    for round in rounds:
        opponentChoice = round[0]
        playerChoice = round[0]

        if round[1] == 'X':
            playerChoice = WINNING_MATCHUPS[opponentChoice]
        elif round[1] == 'Z':
            playerChoice = LOSING_MATCHUPS[opponentChoice]

        finalScore += PlayRound(opponentChoice, playerChoice)

    print(finalScore)


inFile = open("2022/Day2/data.txt")
data = inFile.readlines()
inFile.close()

Solution1(data)
Solution2(data)