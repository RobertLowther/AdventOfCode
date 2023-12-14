import math


nodeDict = {}
instructions = ""


class Node:
    def __init__(self, name:str, left:'Node' = None, right:'Node' = None):
        self.name = name
        self.SetChildren(left, right)


    def SetChildren(self, left:'Node' = None, right:'Node' = None):
        self.left = left
        self.right = right


    def GetChild(self, child:str):
        if child == "L":
            return self.left
        elif child == "R":
            return self.right
        else:
            print(f"Argument 'child' of GetChild should be either 'L' or 'R': Entered {child}")
            return None


def Solution1():
    #Navigate Nodes
    currNode = [nodeDict[node] for node in nodeDict if nodeDict[node].name == "AAA"]    
    steps = SolveSteps(currNode)
    print(steps)


def Solution2():
    #Get Starting Nodes
    startNodes = [nodeDict[node] for node in nodeDict if nodeDict[node].name.endswith("A")]

    #Navigate Nodes
    lcm = 1
    for node in startNodes:
        print(f"lcm({lcm}, {SolveSteps(node)}) = {math.lcm(lcm, SolveSteps(node))}")
        lcm = math.lcm(lcm, SolveSteps(node))

    print(lcm)


def SolveSteps(node: Node):
    #Navigate Nodes
    steps = 0
    instructionCount = len(instructions)

    while(not node.name.endswith("Z")):
        dir = instructions[steps % instructionCount]        
        node = node.GetChild(dir)
        steps += 1

    return steps


if  __name__ == '__main__':
    inFile = open("2023/Day8/data.txt")
    data = [line.strip() for line in inFile.readlines()]
    inFile.close()

    # extract instruction set
    instructions = data[0]

    # delete uncessary lines
    data = data[2:]

    # build node dict to ensure that all nodes exist
    for line in data:
        nodeName = line[:3]

        nodeDict[nodeName] = Node(nodeName)

    # link all nodes
    for line in data:
        nodeName, links = line.split(" = ")
        lNodeName = links[1:4]
        rNodeName = links[-4:-1]

        nodeDict[nodeName].SetChildren(nodeDict[lNodeName], nodeDict[rNodeName])


    #Solution1()
    Solution2()
