class Pipe:
    def __init__(self, pos: list[int], conn1: tuple, conn2: tuple, char: str):
        self.position = pos
        self.connections = [conn1, conn2]
        self.char = char
        self.distance = -1
        self.enclosed = False

    def __repr__(self) -> str:
        return self.char


class Map:
    def __init__(self, width, height):
        self.map: list[list[Pipe]] = [[None for x in range(width)] for y in range(height)]
        self.start = None


    def AddPipe(self, pipe: Pipe, pos: list[int]) -> None:
        x = pos[0]
        y = pos[1]

        if 0 <= y < len(self.map) and 0 <= x < len(self.map[0]):
            self.map[y][x] = pipe


    def get_pipe(self, pos) -> Pipe:
        if isinstance(pos, Pipe): return pos

        x, y = pos[0], pos[1]

        if not (0 <= x < len(self.map[0]) and 0 <= y < len(self.map)):
            return None
    
        return self.map[y][x]
    

    def ApplyConnections(self):
        self.start = self.get_pipe(self.start)
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                pipe = self.map[y][x]
                if not pipe:
                    continue
            
                for i in range(len(pipe.connections)):
                    pipe.connections[i] = self.get_pipe(pipe.connections[i])
                    if pipe.connections[i] == None:
                        self.map[y][x] = None
                        break


    def __repr__(self) -> str:
        res = ""
        for row in self.map:
            for col in row:
                res += col.char if col else '.'
            res += "\n"
        return res
    

    def markEnclosedTiles(self):
        stack = [self.start]
        visited = set()

        while stack:
            current_pipe = stack.pop()
            x, y = current_pipe.position

            if (x, y) in visited or current_pipe.char == '.':
                continue

            visited.add((x, y))
            current_pipe.enclosed = True

            for neighbor_pos in current_pipe.connections:
                neighbor_pipe = self.get_pipe(neighbor_pos)
                if neighbor_pipe and not neighbor_pipe.enclosed:
                    stack.append(neighbor_pipe)



    def countEnclosedTiles(self):
        count = 0
        for row in self.map:
            for pipe in row:
                if pipe and pipe.enclosed:
                    count += 1
        return count


def expandData(data):
    newData = []

    # construct new data of apropriate size
    for y in range(len(data)):
        newData.append([])
        newData.append([])
        for x in range(len(data[0])):
            newData[-1].append(" ")
            newData[-1].append(" ")
            newData[-2].append(data[y][x])
            newData[-2].append(" ")

    for y in range(len(newData)):
        for x in range(len(newData[0])):
            char = newData[y][x]
            if not char == " ": continue

            up = "+"
            down = "+"
            right = "+"
            left = "+"

            if x > 0: left = newData[y][x-1]
            if x < len(newData[0]) - 1: right = newData[y][x+1]
            if y > 0: up = newData[y-1][x]
            if y < len(newData) - 1: down = newData[y+1][x]

            if up in "F7|" and down in "J|L":
                newData[y][x] = "|"
            elif left in "F-L" and right in "J-7":
                newData[y][x] = "-"
            elif up in "F7|" and right in "J-7":
                newData[y][x] = "L"
            elif up in "F7|" and left in "F-L":
                newData[y][x] = "J"
            elif down in "J|L" and right in "J-7":
                newData[y][x] = "F"
            elif down in "J|L" and left in "F-L":
                newData[y][x] = "7"
            else:
                newData[y][x] = " "

    return newData


def simplifyMap(data, start):
    stack = [start]

    while stack:
        next = stack.pop()
        char = data[next[1]][next[0]]

        n1 = [next[0], next[1]]
        n2 = [next[0], next[1]]
        
        if char in "+.":
            continue
        elif char == "F":
            n1[0] += 1
            n2[1] += 1
        elif char == "7":
            n1[0] -= 1
            n2[1] += 1
        elif char == "J":
            n1[0] -= 1
            n2[1] -= 1
        elif char == "L":
            n1[0] += 1
            n2[1] -= 1
        elif char == "|":
            n1[1] += 1
            n2[1] -= 1
        elif char == "-":
            n1[0] += 1
            n2[0] -= 1

        stack.append(n1)
        stack.append(n2)

        data[next[1]][next[0]] = '+'
        
    for y in range(len(data)):
        for x in range(len(data[0])):
            if not data[y][x] in "+.":
                data[y][x] = " "

    return data


def Solution1(data: list[str]):
    pipeMap = Map(len(data[0]), len(data))

    # Fill out pipe map
    for y in range(len(data)):
        line = data[y]
        for x in range(len(line)):
            char = line[x]
            if char == '.':
                continue
            
            pos = [x, y]
            conn1 = [x, y]
            conn2 = [x, y]

            if char == "S":
                pipeMap.start = [x, y]
            elif char == "F":
                conn1[0] += 1
                conn2[1] += 1
            elif char == "7":
                conn1[0] -= 1
                conn2[1] += 1
            elif char == "L":
                conn1[0] += 1
                conn2[1] -= 1
            elif char == "J":
                conn1[0] -= 1
                conn2[1] -= 1
            elif char == "-":
                conn1[0] -= 1
                conn2[0] += 1
            elif char == "|":
                conn1[1] -= 1
                conn2[1] += 1

            pipe = Pipe(pos, conn1, conn2, char)
            if conn1 == conn2: pipe.distance = 0
            pipeMap.AddPipe(pipe, pos)

    # Check that a start position was found
    if pipeMap.start == None:
        print("ERROR: Start position not found")
        return
    
    # find the connections to start
    startX, startY = pipeMap.start
    neighbors = [pipeMap.get_pipe([startX, startY - 1]),
                 pipeMap.get_pipe([startX + 1, startY]),
                 pipeMap.get_pipe([startX, startY + 1]),
                 pipeMap.get_pipe([startX - 1, startY])]
    
    pipeMap.get_pipe([startX, startY]).connections = [n.position for n in neighbors if n and pipeMap.start in n.connections]

    pipeMap.ApplyConnections()

    path = [pipeMap.start]

    while len(path) > 0:
        current_pipe = path.pop(0)
        for neighbor_pipe in current_pipe.connections:            
            if neighbor_pipe.distance == -1:
                neighbor_pipe.distance = current_pipe.distance + 1
                path.append(neighbor_pipe)

    # Find the maximum distance in the loop
    max_distance = max(pipe.distance for row in pipeMap.map for pipe in row if pipe)

    print(f"Maximum Distance: {max_distance}")


def Solution2(data: list[str]):
    data = [[c for c in line] for line in data]
    print(data[50][64])
    start = [50, 64]

    data = expandData(data)
    data = simplifyMap(data, start)

    for y in range(len(data)):
        for x in range(len(data[0])):
            print(data[y][x], end = "")
        print()
    print()



if  __name__ == '__main__':
    inFile = open("2023/Day10/data.txt")
    data = [line.strip() for line in inFile.readlines()]
    inFile.close()

    Solution1(data)
    Solution2(data)
