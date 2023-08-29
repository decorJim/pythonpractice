class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if 1 <= len(haystack) and len(needle) <= 104:       # check if length of both string are within correct size
          if len(haystack)<len(needle):                     # we cannot have a substring longer than the string itself
              return -1
          for i in range(len(haystack)):                    # start by setting i as a starting character in the haystack
              counter=0                                     # counter to keep track of how many matching character we have
              k=i                                           # pointer k will advance in the haystack when we get a match
              j=0                                           # pointer j will advance in the needle to keep track of the wanted characters
              while k<len(haystack) and haystack[k]==needle[j] and counter<len(needle): 
                counter+=1                                  # increment counter when we get a match
                if len(needle)==1:                          # if we only have a single character then we found our answer
                   return i 
                if counter==len(needle):                    # if length needle>1 we send our starting position when the counter reaches the lenght of the needle
                   return i
                k+=1                                        # increment both pointers to check if next character is a match
                j+=1
          return -1                                         # the string does not contain the wanted substring