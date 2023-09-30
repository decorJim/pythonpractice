class Solution:
    def isHappy(self, n: int) -> bool:
       marked=set()

       while n not in marked:           # while we cannot find the next number in set 
           marked.add(n)                # add it to the set
           n=self.computeNextNum(n)     # compute the next one
           if n==1:
               return True              #  if it is 1 return true
       return False                     #  if we find the next number in set we break out of while
                                        #  knowing it will loop endlessly on numbers not 1
                                        # outside while we return false


    def computeNextNum(self,n:int)->int:
        nextNum=0                        
        num=str(n)                       # convert number into string
        for i in range(len(num)):        # access each digit 
            nextNum+=pow(int(num[i]),2)  # take square of each digit and sum them together
        return nextNum      