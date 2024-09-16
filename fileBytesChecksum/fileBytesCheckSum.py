"""
Given a list of integers where the first element of each chunk represents the size of the chunk 
and the subsequent elements are the chunk's contents, write a function that computes the sum of 
each chunk's contents and returns a list of these sums.

fileBytes = [3, 234, 543, 19, 2, 32, 67]
the first element 3 tells us that the next three elements
234, 543, 19 belong to the chunk.

so ans = [796, 99]
"""


from typing import List


def checkSum(fileBytes: List[int]):
    
    chunkIt = 0
    ans = []

    # code is O(n) time complexity since the outer loop does not revisit elements
    # that has already been visited it jumps directly to the next size

    while chunkIt < len(fileBytes):
        
        currentSum = 0
        chunkSize = fileBytes[chunkIt]

        # place pointer at index next to current one which is the size
        i = chunkIt + 1

        # chunkIt points to the size if we add chunkSize to the index we 
        # get the last element of the chunk. By adding 1 again we get 
        # the index of the next size that is also the length we need
        # for i to consider the last element
        size = chunkIt + chunkSize + 1
        while i < size:
            currentSum += fileBytes[i]
            i += 1

        ans.append(currentSum)
        chunkIt += chunkSize + 1


    return ans

    
fileBytes=[3, 234, 543, 19, 2, 32, 67]
print(checkSum(fileBytes))





                





    






               



           
    

            

   







    






















    


        


