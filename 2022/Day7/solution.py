class file:
    def __init__(self, name:str, size:int):
        self.name = name
        self.size = size

    def __repr__(self) -> str:
        return f"{self.name} (file, size={self.size})"
    
    def __str__(self) -> str:
        return f"{self.name} (file, size={self.size})"


class dir:
    def __init__(self, name:str, parent:'dir'):
        self.name = name
        self.parent = parent
        self.size = 0
        self.files = []
        self.dirs = []


    def GetFile(self, name:str):
        for f in self.files:
            if f.name == name:
                return f
        return None


    def GetDir(self, name:str):
        for d in self.dirs:
            if d.name == name:
                return d
        return None
    

    def AddDir(self, d: 'dir'):
        self.dirs.append(d)
    
    
    def AddFile(self, f: file):
        self.files.append(f)
        self.ChangeSize(f.size)


    def ChangeSize(self, diff: int):
        self.size += diff
        if self.parent: self.parent.ChangeSize(diff)


    def Tree(self, indent="- ", args="-d -f"):
        _args = args.split()
        res = f"{indent}{self}"

        indent = f"  {indent}"
        if "-d" in _args:
            for d in self.dirs:
                res += "\n" + d.Tree(indent, args)

        if "-f" in _args:
            for f in self.files:
                res += f"\n{indent}{f.__str__()}"

        return res


    def __repr__(self) -> str:
        return f"{self.name} (dir, size={self.size})"


root = dir('/', None)
workingDir = root


def Solution1(data: str):
    allDirs: list[dir] = []

    buffer = ''
    
    while len(data) > 0:
        buffer = data.pop(0)

        if buffer.startswith("$"): # This is a command
            command = [s for s in buffer.split() if s != "$"]
            
            if (command[0] == "cd"):
                if len(command) == 1:
                    workingDir = root
                elif command[1] == '/':
                    workingDir = root
                elif command[1] == '..':
                    workingDir = workingDir.parent
                else:
                    nextDir = workingDir.GetDir(command[1])
                    workingDir = nextDir if nextDir else workingDir
            elif (command[0] == "ls"):
                while len(data) > 0 and data[0][0] != "$":
                    details, name = data.pop(0).split()
                    if details == "dir":
                        allDirs.append(dir(name, workingDir))
                        workingDir.AddDir(allDirs[-1])
                    else:
                        workingDir.AddFile(file(name, int(details)))
                        
    sum = 0
    for s in [d.size for d in allDirs if d.size <= 100000]:
        sum += s

    print(sum)

                    
def Solution2(data: str):
    additionalSpaceNeeded = root.size - 40000000
    dirSizes = [int(line.split("=")[1][:-1]) for line in root.Tree(args="-d").split("\n")]
    dirSizes = [i for i in dirSizes if i >= additionalSpaceNeeded]
    dirSizes.sort()
    print(dirSizes[0])


inFile = open("2022/Day7/data.txt")
data = [line.strip() for line in inFile.readlines()]
inFile.close()

Solution1(data)
Solution2(data)
