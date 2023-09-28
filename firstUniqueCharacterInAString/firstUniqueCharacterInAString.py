class Solution:
    def firstUniqChar(self, s: str) -> int:
       frequency={}                         # keeps track of how many occurence a character has in s
       indexes={}                           # stores the index of each first character

       for i in range(len(s)):
           if s[i] in frequency:
              frequency[s[i]]+=1            # if character already exist then increase the frequency count
           else: 
              frequency[s[i]]=1             # else it occurred once
              indexes[s[i]]=i               # map the character to its index
        
       for character in frequency:          # by default hashset and hashmap are already sorted
            if frequency[character]==1:     # when meeting the first character with a count of 1
                return indexes[character]   # extract its index from the hashmap with indexes
       return -1                            # cant find anything then return -1