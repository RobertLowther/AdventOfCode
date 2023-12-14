def Solution1(data: list[str]):
    crateData = []
    columnCount = 0

    while(data[0] != ""):
        if not data[0][1].isnumeric():
            crateData.append(data[0])
        else:
            columnCount = int(data[0].split()[-1])
        data = data[1:]

    data = data[1:]

    stacks = [[] for x in range(columnCount)]

    while len(crateData) > 0:
        row = crateData.pop()
        for i in range(columnCount):
            start = i*4
            crate = row[start:start + 3]
            if crate != "   ":
                stacks[i].append(crate)

    for command in data:
        command = [int(i) for i in command.split() if i.isnumeric()]
        
        for i in range(command[0]):
            crate = stacks[command[1] - 1].pop()
            stacks[command[2] - 1].append(crate)

    result = ""
    for i in range(columnCount):
        result += stacks[i][-1][1]

    print(result)


def Solution2(data: list[str]):
    crateData = []
    columnCount = 0

    while(data[0] != ""):
        if not data[0][1].isnumeric():
            crateData.append(data[0])
        else:
            columnCount = int(data[0].split()[-1])
        data = data[1:]

    data = data[1:]

    stacks = [[] for x in range(columnCount)]

    while len(crateData) > 0:
        row = crateData.pop()
        for i in range(columnCount):
            start = i*4
            crate = row[start:start + 3]
            if crate != "   ":
                stacks[i].append(crate)

    for command in data:
        command = [int(i) for i in command.split() if i.isnumeric()]
        
        count = command[0]
        src = command[1] - 1
        dst = command[2] - 1

        crates = stacks[src][-count:]
        stacks[src] = stacks[src][:-count]
        stacks[dst] += crates

    result = ""
    for i in range(columnCount):
        result += stacks[i][-1][1]

    print(result)


inFile = open("2022/Day5/data.txt")
data = [line.strip('\n') for line in inFile.readlines()]
inFile.close()

Solution1(data)
Solution2(data)
