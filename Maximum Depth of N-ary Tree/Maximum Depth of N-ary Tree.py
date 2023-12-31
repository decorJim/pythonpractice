"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def maxDepth(self, root: 'Node') -> int:
        return self.dfs(root) # pass the root node
    
    def dfs(self,node:'Node')->int:
        if node==None:              # if the current passed node is null then we know
           return 0                 # his parent is a leaf node
        
        depth=0                     # will be set by the loop
                                    # ex: child1:2 child2:1 child3:3    depth=3 
        for i in node.children:
           depth=max(depth,self.maxDepth(i))  # a given node I check which of the children has more depth
                                              # like finding max in array we call maxDepth to indirectly call dfs for child nodes
        return 1+depth              # current node adds a level to its child's depth so 3+1
        

        # when function reaches the child of a leaf node aka None, None Node will return 0 in self.maxDepth
        # the first leaf node will compare max(depth,0) they both are 0 so depth=0
        # when leaf node return his depth to his parent node we increase of 1 level so depth+1 (0+1)
        # parent node compares this depth with other child to see which is higher
        # then overwrite his own depth and adds 1 to it for his own parent