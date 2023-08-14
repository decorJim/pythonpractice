class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet=set()
        res=0
        i=0     # left pointer

        for j in range(len(s)):       # right pointer
           while s[j] in charSet:     # if we have a duplicate on the right side of sliding window
               charSet.remove(s[i])   # keep removing the elements from the set
               i+=1                   # keep shrinking sliding window on the left side move left pointer by one
           
           charSet.add(s[j])          # after sliding window no longer has any duplicate, add the new element to the set
           res=max(res,i-j+1)         # check if lenght of current window is longer than current max length
        
        return res