
def programLoop1(inputList):
    accum = 0
    visited = []

    index = 0

    while not index in visited:
        
        #break for part 2
        if index == len(inputList):
            break

        currentInstruction = inputList[index].split(" ")[0]
        currentNumber = inputList[index].split(" ")[1]
        if currentNumber[0] == '+':
            currentNumber = int(currentNumber[1:])
        else:
            currentNumber = -int(currentNumber[1:])

        
        if (currentInstruction == "acc"):
            accum += currentNumber
            visited.append(index)
            index += 1
        
        elif (currentInstruction == "nop"):
            visited.append(index)
            index += 1
        elif (currentInstruction == "jmp"):
            visited.append(index)
            index += currentNumber

    return (accum,visited,index)

def programLoop2(inputList):
    
    accum = 0
    visited = programLoop1(inputList)[1]
    index = 0
    indexToSwap = 0
    
    while (index != len(inputList)):
        
        for i in range(0, len(visited)):

            if index == len(inputList):
                break
            mutable_inputList = inputList

            currentInstruction = inputList[visited[i]].split(" ")[0]
            currentNumber = inputList[visited[i]].split(" ")[1]

            if currentInstruction == "jmp":
                mutable_inputList[visited[i]] = "nop " + currentNumber
                indexToSwap = visited[i]
                accum, index = programLoop1(mutable_inputList)[0], programLoop1(mutable_inputList)[2]

            elif currentInstruction == "nop":
                mutable_inputList[visited[i]] = "jmp " + currentNumber
                indexToSwap = visited[i]
                accum, index = programLoop1(mutable_inputList)[0], programLoop1(mutable_inputList)[2]
    
    return (accum, indexToSwap)

def part1():
    
    f = open('day8/inputDay8.txt', 'r')

    inputList = []

    #cleanup, removes newlines
    for line in f:
        cleaned_line = line.strip()
        inputList.append(cleaned_line)

    print("Part 1: Accum = " + str(programLoop1(inputList)[0]))


def part2():
    f = open('day8/inputDay8.txt', 'r')

    inputList = []

    #cleanup, removes newlines
    for line in f:
        cleaned_line = line.strip()
        inputList.append(cleaned_line)

    accum, swapIndex = programLoop2(inputList)[0], programLoop2(inputList)[1]
    
    print("Part 2: Accum = " + str(accum))
    print("Index to swap: " + str(swapIndex))
    
    
part1()
part2()