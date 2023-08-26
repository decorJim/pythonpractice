class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1    # setup each pointer as far from each other as possible to increase chance to get max width
        maxArea=0              # set a max variable
        while i<j:
           if (j-i)*min(height[i],height[j])>maxArea:   # if the combination of width*height>current max replace it
               maxArea=(j-i)*min(height[i],height[j])
           if height[i]==height[j]:                     # if both height are the same just move the i pointer nothing changes if we move either
               i+=1
           if height[i]<height[j]:                      # we want to maximize height so move the pointer with the minimum height
               i+=1                                     # since it is the limiting factor and water will spill 
           else:
               j-=1
        return maxArea

  
            
            
  
            
            