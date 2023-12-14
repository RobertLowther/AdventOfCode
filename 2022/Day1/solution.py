inFile = open("2022/Day1/data.txt")
data = [line.strip() for line in inFile.readlines()]
inFile.close()

data.append("")

def solution1():
    maxCalories = 0
    calorieCount = 0

    for line in data:
        if line == "":
            if calorieCount > maxCalories:
                maxCalories = calorieCount
            calorieCount = 0
        else:
            calorieCount += int(line)

    print(maxCalories)


def solution2():
    caloriesHeld = []
    calorieCount = 0

    for line in data:
        if line == "":
            caloriesHeld.append(calorieCount)
            calorieCount = 0
        else:
            calorieCount += int(line)

    caloriesHeld.sort()

    sumOfTopThree = 0
    for i in range(1, 4):
        sumOfTopThree += caloriesHeld[-i]

    print(sumOfTopThree)


solution1()
solution2()