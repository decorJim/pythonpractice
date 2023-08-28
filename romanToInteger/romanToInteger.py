class Solution:
    def romanToInt(self, s: str) -> int:
        map={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000} # maps what each symbol represents
        if 1<=len(s)<=15:      
          val=0                   # variable to store the actual value
          i=0
          while i<len(s):  
            if i==len(s)-1:           # = since last character does not have an i+1 so if map.get(s[i+1])>map.get(s[i]): will fail
                val+=map.get(s[i])    # if pointer is at last symbol add the corresponding value and break out of the loop
                break
            if map.get(s[i+1])>map.get(s[i]):         # if the symbol coming after the current symbol has a higher value, substract the next value by the current value
                val+=map.get(s[i+1])-map.get(s[i])    # ex: IV take 5-1=4
                i+=2                                  # skip the next iteration
            else:
                val+=map.get(s[i])                    # if the values that comes after are smaller just add them to the total
                i+=1
          return val