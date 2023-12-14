def checkForRepeats(seq: str):
    for i in range(len(seq) - 1):
        for j in range(i+1, len(seq)):
            if seq[i] == seq[j]:
                return True
            
    return False

def Solution1(data: str):
    lastFour = " " + data[:3]

    for i in range(3, len(data)):
        lastFour = lastFour[1:]
        lastFour += data[i]
        if not checkForRepeats(lastFour):
            print(i + 1)
            return

def Solution2(data: str):
    last14 = " " + data[:13]

    for i in range(13, len(data)):
        last14 = last14[1:]
        last14 += data[i]
        if not checkForRepeats(last14):
            print(i + 1)
            return


inFile = open("2022/Day6/data.txt")
data = inFile.read()
inFile.close()

Solution1(data)
Solution2(data)
