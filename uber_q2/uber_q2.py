from typing import List


def solution(a2b: List[int], b2a: List[int], trips: int):

    nbTrips = 0
    currentTime = 0

    i = 0
    j = 0

    # time complexity O(m + n)
    # m : length of a2b
    # n : length of b2a
    # worst case is in order to complete the number of trips 
    # both pointers have to go through all elements of their respective array

    while nbTrips < trips:

        print("i:",i)
        print("j:",j)
        print()
        
        while a2b[i] < currentTime:
            i += 1

        # we need to wait until departure time anyway so no matter what the current time is 
        # it is going to end up being the departure time + travel time
        currentTime = a2b[i] + 100

        while b2a[j] < currentTime:
            j += 1
        
        currentTime = b2a[j] + 100

        nbTrips += 1

    return currentTime


print(solution([10, 150, 175], [99, 135, 260], 1))
print()

print(solution([0, 200, 500], [99, 210, 450], 1))
print()

print(solution([109, 200, 500], [99, 210, 600], 2))
print()
