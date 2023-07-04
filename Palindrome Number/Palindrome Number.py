class Solution(object):
    """ x is an integer """
    def isPalindrome(self, x):
        if x<0:
            return False

        # a single digit is always a palindrome
        elif x<10 :
            return True
        
        tab=[]
        while x>0:
            # by using modulus we can extract the last digit from a number
            tab.append(x%10)
            # remove last digit from original number
            x=(x-x%10)/10
        
        i,j=0,len(tab)-1
        while i<j:
            if tab[i]!=tab[j]:
                return False
            i+=1
            j-=1
            
        return True