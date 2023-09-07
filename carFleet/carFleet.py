class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        map={}
        for i in range(len(position)):   # stores all initial position mapped to respective car speed
            map[position[i]]=speed[i]    # map keys are not ordered
        
        keys=list(map.keys())            # extract keys from map
        keys.sort()                      # sort keys

        sortedMap={ i:map[i] for i in keys }  # create a sorted map from smallest initial position to highest

        stack=[]                              # stores all leading cars that prevent cars catching up to pass them

        for i in keys[::-1]:                  # [::-1] iterate in reverse order
            stack.append((target-i)/sortedMap[i])      # stores the time needed to reach target destination (target-initial position)/speed
            if len(stack)>=2 and stack[-1]<=stack[-2]: # if the time needed of current car ([-1] top of the stack) is smaller than the one in front of him aka he will catch up to him 
                stack.pop()                            # the one in front of the current will become a leading car so remove the current car's time
        return len(stack)                     # the total length of the stack represents the number of leading cars