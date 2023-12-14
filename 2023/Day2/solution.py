infile = open("2023/Day2\\data.txt")
possibleGames = []
powers = []

for line in infile.readlines():
    red = 0
    green = 0
    blue = 0

    id, rounds = line.split(":")
    id = int(id.split()[-1])
    rounds = rounds.split(";")

    print(f"Game {id}: {len(rounds)} rounds")

    for round in rounds:
        print("\t", end="")
        groups = round.split(",")
        for i in range(len(groups)):
            count, color = groups[i].split()
            count = int(count)
            if color == "red" and count > red: red = count
            if color == "green" and count > green: green = count
            if color == "blue" and count > blue: blue = count
            print(groups[i], end="")
            if i < len(groups) - 1: print(",", end="")
        print()

    print(f"\tMax: red {red}, green {green}, blue {blue}")
    if (red <= 12 and green <= 13 and blue <= 14): possibleGames.append(id)
    powers.append(red * green * blue)

infile.close()

possibiltySum = 0
powerSum = 0

for i in possibleGames: possibiltySum += i
for i in powers: powerSum += i

print(f"Sossible Game Sum - {possibiltySum}")
print(f"Game Power Sum - {powerSum}")