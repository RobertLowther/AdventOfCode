import re
import math

f = open("2023/Day5/data.txt", "r")
lines = f.read().splitlines()
f.close()

seeds = []
mapRanges = []
seedRanges = []

# Dealing with the inputs
seeds = [int(i) for i in lines[0].split() if i.isnumeric()]
for x in range(0, len(seeds), 2):
    seedRanges.append([seeds[x], seeds[x+1]])

lines = lines[3:]

# saving ranges to array
tempRange = []
for line in lines:
    # New type of map starts
    if(re.search(r'map', line)):
        mapRanges.append(tempRange)
        tempRange = []
    else:
        if(len(line) > 0):
            tempRange.append([int(i) for i in line.split()])
mapRanges.append(tempRange)
mapRanges.reverse()

#Map checking
x = -1
found = False
while(not found):
    x += 1
    currentMap = x
    for i in mapRanges:
        for j in i:
            if(j[0] <= currentMap < j[0] + j[2]):
                currentMap = j[1] + (currentMap - j[0])
                break
    # Checking if seed is in any starting range

    for i in seedRanges:
        if(i[0] <= currentMap < i[0] + i[1]):
            found = True

print(x)