def isValidPalindrome(s:str)->bool:
   # O(n)
   s="".join(char for char in s if char.isalnum())
   s=s.lower()
   print("is alpha numerical",s)

   if len(s)==0:
      return True
   if len(s)==1:
      return True

   # place i at beginning index and j at last index
   i,j=0,len(s)-1

   # aabaa 
   # O(n)
   while(i<j):
      if s[i]!=s[j]:
         return False
      i+=1
      j-=1
   return True

s1="A $#man- Has+ 2 Car"
s2=""
s3="a"
s4="A man A"

print(isValidPalindrome(s1))
print(isValidPalindrome(s2))
print(isValidPalindrome(s3))

# O(2n)->O(n) time complexity

