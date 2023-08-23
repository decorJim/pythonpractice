class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxIndexi:int=0    
        maxIndexj:int=0
        maxLength:int=0
        for k in range(len(s)):   # since i and j are going outward we keep track of the origin letter of where the expansion will begin 
            i,j=k,k               # set pointers if length is odd at same spot
            while i>=0 and j<len(s) and s[i]==s[j]:
                if j-i+1>maxLength:          # if current palindrome substring longer replace max
                    maxLength=j-i+1
                    maxIndexi=i              # update index because we don't want to copy substring everytime
                    maxIndexj=j
                i-=1
                j+=1
            i,j=k,k+1                        # set pointers in case length is even j is just one spot after
            while i>=0 and j<len(s) and s[i]==s[j]:
                if j-i+1>maxLength:
                    maxLength=j-i+1
                    maxIndexi=i
                    maxIndexj=j
                i-=1
                j+=1
        res=s[maxIndexi:maxIndexj+1]         # extract substring using indexes

        return res