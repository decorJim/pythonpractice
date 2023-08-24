class Solution:
    def reverse(self, x: int) -> int:
        temp="" # temporary empty string to store the number in reverse order

        negative=False # variable to know if input was negative

        if x<0:
            negative=True
            x=x*-1           # convert number to it's positive counterpart

        x=str(x)             # convert the number to a string
        
        i=len(x)-1           # max index of loop iteration

        while i>=0:
            temp+=x[i]
            i-=1

        reverse=int(temp)

        if negative:
            reverse=reverse*-1
        
        if pow(-2,31) <= reverse <=pow(2,31)-1:
            return reverse
        return 0
        