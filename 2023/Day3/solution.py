class number:
    value : int = 0
    startX : int = -1
    startY : int = -1
    width : int = -1

    boundXMin = 0
    boundXMax = 0
    boundYMin = 0
    boundYMax = 0

    def __init__(self, _value:int, _startX:int, _startY:int):
        self.value = _value
        self.startX = _startX
        self.startY = _startY
        self.width = len(str(self.value))
        self.boundXMin = self.startX - 1
        self.boundXMax = self.startX + self.width
        self.boundYMin = self.startY - 1
        self.boundYMax = self.startY + 1

        if self.startX < 0 or self.startY < 0 or self.value < 0:
            print("Error the number value and starting indexes must be >= 0")
            print(f"value: {self.value}")
            print(f"startX: {self.startX}")
            print(f"startY: {self.startY}")
    
    def IsPartNumber(self, data) -> bool:
        checkWidth = len(str(self.value)) + 2
        checkHeight = 3

        checkXStart = self.startX - 1
        checkXEnd = checkXStart + checkWidth
        checkYStart = self.startY - 1
        checkYEnd = checkYStart + checkHeight
        
        for x in range(checkXStart, checkXEnd):
            if x < 0 or x >= len(data[0]): continue

            for y in range(checkYStart, checkYEnd):
                if y < 0 or y >= len(data): continue

                char = data[y][x]
                if not char.isdigit() and not char == ".":
                    return True

        return False
    
    def Overlap(self, x, y) -> bool:

        return not (self.boundXMax < x or
                    self.boundXMin > x or
                    self.boundYMax < y or
                    self.boundYMin > y)


inFile = open("2023/Day3\\data.txt")
data = inFile.readlines()
inFile.close()

#convert data to 2D array
for i in range(len(data)):
    data[i] = [c for c in data[i].strip()]

#extract all numbers
numbers = []

for lineNum in range((len(data))):
    num = ""
    startX = -1
    line = data[lineNum]

    for i in range(len(line)):
        char = line[i]
        if char.isdigit():
            if num == "": startX = i
            num += char
        elif num != "":
            numbers.append(number(int(num), startX, lineNum))
            num = ""
    if num != "":
        numbers.append(number(int(num), startX, lineNum))

ratios = []
for lineNum in range((len(data))):
    for charNum in range(len(data[lineNum])):
        if data[lineNum][charNum] == "*":
            overlap = []
            for n in numbers:
                if n.Overlap(charNum, lineNum): overlap.append(n)

            if len(overlap) == 2:
                ratios.append(overlap[0].value * overlap[1].value)

result = 0
for ratio in ratios:
    result += ratio

print(f"sum - {result}")