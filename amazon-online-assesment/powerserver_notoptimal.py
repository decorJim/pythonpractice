"""
Find the power of each possible contiguous group of servers.
ex- [2,1,3] - 27
explanation -
power[0,0] = min(2)*sum([2]) = 4
power[0,1] = min(2,1)*sum([2,1]) = 3
power[0,2] = min(2,1,3)*sum([2,1,3]) =6
power[1,1] = min(1)*sum(1) = 1
power[1,2] = min(1,3)*sum([1,3]) = 4
power[2,2] = min(3)*sum([3]) = 9
"""

from typing import List


def power(servers:List[int]):

    allPower = []

    for i in range(len(servers)):

        j = i

        currentMin = servers[i]
        currentSum = servers[j]
        while j < len(servers):
            
            if i != j:

                currentMin = min(currentMin,servers[j])
                currentSum = currentSum + servers[j]

            currentPower = currentMin * currentSum
            allPower.append(currentPower)
          
            j += 1

    return sum(allPower)



print(power([2,1,3]))
    



