stringToIntDict = {
    "zerone": "01",
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def Solution1():
    result = 0

    with open("2023/Day1\\data.txt") as infile:
        for line in infile.readlines():
            curr = -1
            for c in line:
                if c.isdigit():
                    if curr == -1:
                        result += int(c) * 10
                    curr = int(c)

            result += curr

    print(result)

def Solution2():
    result = 0

    with open("2023/Day1\\data.txt") as infile:
        for line in infile.readlines():
            
            #replace spelled numbers with int characters
            for key in stringToIntDict.keys():
                line = line.replace(key, stringToIntDict[key])

            curr = -1
            for c in line:
                if c.isdigit():
                    if curr == -1:
                        result += int(c) * 10
                    curr = int(c)

            result += curr

    print(result)

Solution1()
Solution2()