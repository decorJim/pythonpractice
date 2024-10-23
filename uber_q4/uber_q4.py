from typing import List

def computeInstruction(strIntruction: str):

    if strIntruction[0] == "+":
        return int(strIntruction[1:])
        
    else:
        return -1 * int(strIntruction[1:])


def solution(queries: List[str], diff: int):
        
    numbers = []
    frequencies = {}
    subsets = []
    output = []

    def addSubset(currentSubset):

        for subset in subsets:

            if subset == currentSubset:
                return

        subsets.append(currentSubset)

    def createSubsets(fArray, sArray, tArray):

        for fIndex in fArray:

            for sIndex in sArray:

                for tIndex in tArray:

                    addSubset(set({fIndex, sIndex, tIndex}))

                        

    def checkCondition(nums: List, diff: int):

        lastNum = nums[-1]

        fArray = []
        sArray = []
        tArray = []

        numberSubset = 0

        fArray = frequencies[lastNum]

        if lastNum + diff in frequencies and lastNum + (2*diff) in frequencies:

            sArray = frequencies[lastNum + diff]
            tArray = frequencies[lastNum + (2*diff)]

        elif lastNum - diff in frequencies and lastNum - (2*diff) in frequencies:

            sArray = frequencies[lastNum - diff]
            tArray = frequencies[lastNum - (2*diff)]
        
        elif lastNum - diff in frequencies and lastNum + diff in frequencies:

            sArray = frequencies[lastNum - diff]
            tArray = frequencies[lastNum + diff]


        createSubsets(fArray, sArray, tArray)        
        numberSubset = len(subsets)
        
        return numberSubset
            

    for query in queries:

        instruction = computeInstruction(query)

        if instruction > 0:

            numbers.append(instruction)

            if instruction in frequencies:
                frequencies[instruction].append(len(numbers) - 1)

            else:
                frequencies[instruction] = [len(numbers) - 1]

            value = checkCondition(numbers, diff)

            output.append(value)

        else:

            number = -1*instruction
            indexes = frequencies[number]

            for index in indexes:

                subsets = list(filter(lambda subset: index not in subset, subsets))

            output.append(len(subsets))

    return output



print(solution(["+4","+5","+6","+4","+3", "-4"], 1))




