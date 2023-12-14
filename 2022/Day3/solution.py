def GetPriority(char: chr):
    ordinal = ord(char)
    if ordinal >= 65 and ordinal <= 90:
        return ordinal - 38
    elif ordinal >= 97 and ordinal <= 122:
        return ordinal - 96
    
    return 0


def Solution1(data: list[str]):
    res = 0

    for line in data:
        pocket1 = line[:int(len(line)/2)]
        pocket2 = line[int(len(line)/2):]

        intersection = set(pocket1).intersection(pocket2)
        
        for i in intersection:
            res += GetPriority(i)

    print(res)


def Solution2(data: list[str]):
    res = 0

    for i in range(0, len(data), 3):
        intersection = set(data[i]).intersection(data[i+1]).intersection(data[i+2])
        
        for i in intersection:
            res += GetPriority(i)
        
    print(res)


inFile = open("2022/Day3/data.txt")
data = [line.strip() for line in inFile.readlines()]
inFile.close()

Solution1(data)
Solution2(data)