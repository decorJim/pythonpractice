from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    print("inputs", intervals)
    print()

    ans = []

    if len(intervals) == 0:
        return ans
    
    if len(intervals) == 1:
        return intervals
    
    # sort every interval by their lower bound
    # so when we iterate we always go front smallest to largest
    intervals.sort(key = lambda i:i[0])

    print("sorted", intervals)
    print()

    # put first interval in to start algorithm
    ans.append(intervals[0])

    # since we put first interval in first we start at 1
    i = 1
    
    while i < len(intervals):

        back = ans[-1]
        front = intervals[i]

        # if the last interval in ans has equal or bigger
        # upper bound than the lower bound of current interval
        # [1,3] [2,4] -> [1,4]
        # [1,3] [3,4] -> [1,4]
        if back[1] >= front[0]:

            # first remove the last element in ans first since the interval
            # is going to be merge 
            ans.pop()

            # compare which upper bound is bigger
            # either [1,3] [2,4]
            upperValue = max(back[1], front[1])

            # add new merged interval in
            ans.append([back[0], upperValue])

        else:

            ans.append(intervals[i])

        i += 1

    return ans

print(merge([[1,3]]))
print()

print(merge([[1,4],[0,4]]))
print()

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print()

print(merge([[1,4],[0,1]]))
print()