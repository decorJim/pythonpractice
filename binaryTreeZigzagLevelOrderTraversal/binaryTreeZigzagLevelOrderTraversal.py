# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[] # stores all array
        # in this problem we will use a deque to act like a queue
        # we only need smt with FIFO
        # deque can insert from both ends
        q=deque([root] if root else []) # if there is a root add it else add empty array

        # q stores all nodes of the current level

        while q:       # while queue not empty this loop makes sure we reach the last level of tree BY CONSTANTLY ADDDING NODE OF NEXT LEVEL q IS NOT EMPTY
           level=[]
           for i in range(len(q)):         # In python the length of the queue will autoupdate
               node=q.popleft()            # [C,B,A] -> [B,A]
               level.append(node.val)      # take the value of current node and put it inside level array
               if node.left:
                   q.append(node.left)     # add to the right left child BY ADDING NEW ELEMENTS ONCE FOR REACHES END WHILE WILL DETECT q IS NOT EMPTY AND START ITERATION FOR NEXT LEVEL
               if node.right:
                   q.append(node.right)    # add to the right right child

           if len(res)%2==1:
                level=reversed(level)      # all odd level must be print in reverse order horizontal
           res.append(level)               
        return res
