
from typing import List


def checkSum(fileBytes:List[int]):
    #
    # [3,234,543,19,2,32,67]
    #  i j->     -  i j-> -
    #
    #  tricky part is counter is not the subpointer j
    #  counter only checks if we have accessed all content 
    #  if size of chunk is 3 counter checks if we counted all 3
    #  j is made to access each individual content in the chunk so 234,543,19
    #  i just keeps track of the next metadata of the chunk

    checksums=[]

    i=0
    while i<len(fileBytes):
        size=fileBytes[i]
        sum=0
        j=i+1
        counter=0
        while counter<size:
            sum+=fileBytes[j]
            counter+=1
            j+=1
        checksums.append(sum)
        i=i+size+1
    return checksums



fileBytes=[3,234,543,19,2,32,67]
print(234+543+19)
print(32+67)
print(checkSum(fileBytes))





                





    






               



           
    

            

   







    






















    


        


