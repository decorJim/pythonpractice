
"""
For SalesData = [ 1 1 1 2 2 3 3 4 4 4 ], frequencyThreshold = 2
output: 8

so we want the longuest subarray with different repeated number
in our case 2 
[ 1 1 2 2 3 3 4 4 ] this is the longuest subarray with each number repeated frequencyThreshold times
its length is 8

each pair is unique

"""

def solution(salesData, frequencyThreshold):

    i = 0
    j = 0

    frequencies = {}

    maxLen = 0

    while j < len(salesData):

        if salesData[j] in frequencies:
            frequencies[ salesData[j] ] += 1
        
        else:
            frequencies[ salesData[j] ] = 1


        # map keep tracks of consecutive continuous number
        # if the frequencyThreshold then move the left pointer until all frequencies are lower
        while any(frequency > frequencyThreshold for frequency in frequencies.values()):

            # by moving left pointer we are no longer including the far left frequency
            #  1:3  <- the i now points to the second 1 so reduce frequency to 2
            #  2:2
            #  3:2
            frequencies[salesData[i]] -= 1

            if frequencies[salesData[i]] == 0:
                del frequencies[salesData[i]]

            i += 1

        maxLen = max(maxLen, j - i + 1)

        j += 1

    return maxLen

# 1 1 2 2 3 3 4 4
print(solution([1,1,1,2,2,3,3,4,4,4], 2))
print()

# 2 2 1 1 3 3 
print(solution([1,1,1,2,2,1,1,3,3,3], 2))
print()