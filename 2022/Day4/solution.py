def Solution1(data: list[str]):
    fullyContained = 0

    for line in data:
        elf1, elf2 = [[int(i) for i in pair.split('-')] for pair in line.split(',')]

        if ((elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or
            (elf1[0] <= elf2[0] and elf1[1] >= elf2[1])):
            fullyContained += 1
    
    print(fullyContained)


def Solution2(data: list[str]):
    overlapped = 0

    for line in data:
        elf1, elf2 = [[int(i) for i in pair.split('-')] for pair in line.split(',')]

        if (elf1[0] <= elf2[1] and elf1[1] >= elf2[0]):
            overlapped += 1
    
    print(overlapped)


inFile = open("2022/Day4/data.txt")
data = [line.strip() for line in inFile.readlines()]
inFile.close()

Solution1(data)
Solution2(data)