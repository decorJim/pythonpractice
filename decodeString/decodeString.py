class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]                                          # stack to store every character inside the string
        for i in range(len(s)):
            if s[i]==']':                                 # at the first occurence of ]
               tempString,num="","" 
               while stack[-1]!='[':                      # go backward to construct substring to repeat until we reach a [
                    tempString=stack.pop()+tempString
               stack.pop()                                # pop the [ once we reach it
               while stack and stack[-1].isdigit():       # go backward while stack is not empty and top of stack is digit again to construct 
                    num=stack.pop()+num                   # the number we need to multiply the substring by
               stack.append(int(num)*tempString)
            else:
               stack.append(s[i])                         # if current character is not ] just keep stacking it
        return "".join(stack)                             # convert the stack into a string 