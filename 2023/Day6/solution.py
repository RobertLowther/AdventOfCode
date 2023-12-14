from math import ceil


class Race:
    def __init__(self, durration: int, highScore: int):
        self.durration = durration
        self.highScore = highScore

def winningMoveCount(race: Race) -> int:
    waysToWin = -1

    losingMoves = 2
    higherCheck = ceil((race.durration-1) / 2)
    lowerCheck = 1

    while(True):
        if higherCheck - lowerCheck == 1:
            losingMoves += lowerCheck * 2
            break

        nextCheck = ceil((lowerCheck + higherCheck) / 2)
        distance = nextCheck * (race.durration - nextCheck)

        if distance == race.highScore:
            losingMoves += nextCheck * 2
            break
        elif distance < race.highScore:
            lowerCheck = nextCheck
        else:
            higherCheck = nextCheck

    waysToWin = race.durration - losingMoves + 1
    return waysToWin

def solution1():
    inFile = open("2023/Day6/data.txt", "r")
    data = [[int(value) for value in line.strip()[11:].split()] for line in inFile.readlines()]
    inFile.close()
    print(data)
    
    winningMoves = 1

    for i in range(len(data[0])):
        winningMoves *= winningMoveCount(Race(data[0][i], data[1][i]))

    print(winningMoves)

def solution2():
    inFile = open("2023/Day6/data.txt", "r")
    data = [int(line.strip()[11:].replace(" ", "")) for line in inFile.readlines()]
    inFile.close()
    race = Race(data[0], data[1])

    print(winningMoveCount(race))

solution1()
solution2()