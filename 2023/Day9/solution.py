data: list[str] = []


class Sequence:
    def __init__(self, values: list[int]):
        self.values = values
        self.analysis = None

        if values[0] != 0 or len(set(values)) != 1:
            tmp = []
            for i in range(1, len(values)):
                tmp.append(values[i] - values[i-1])

            self.analysis = Sequence(tmp)

    def PredictNext(self) -> int:
        if self.analysis == None:
            return self.values[-1]
        else:
            return self.values[-1] + self.analysis.PredictNext()

    def PredictPast(self) -> int:
        if self.analysis == None:
            return self.values[0]
        else:
            return self.values[0] - self.analysis.PredictPast()


def Solution1():
    sum = 0
    for line in data:
        line = [int(i) for i in line.split()]
        
        sum += Sequence(line).PredictNext()

    print(sum)

def Solution2():
    sum = 0
    for line in data:
        line = [int(i) for i in line.split()]
        
        sum += Sequence(line).PredictPast()

    print(sum)


if  __name__ == '__main__':
    inFile = open("2023/Day9/data.txt")
    data = [line.strip() for line in inFile.readlines()]
    inFile.close()

    Solution1()
    Solution2()
