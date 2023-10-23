#        example of bfs
#
#        bfs has no recursive call unlike dfs
#        depends on queue not being empty
#        put all nodes of a level inside
#        

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def bfs(root:Optional[TreeNode]):

    if root==None:
        return []

    tree=[]
    
    # if the given root node is not empty
    queue=deque([root] if root else [])

    while queue:

        level=[]
        
        # traverse all node of the current level stored in queue
        for _ in range(len(queue)):
            
            # get the node at the front of the queue
            node=queue.popleft()

            level.append(node.val)

            # If the tree can have more than 2 child this part will be a for loop instead
            # left child node exist, add to queue
            if node.left:

               queue.append(node.left)

            # right child node exist, add to queue
            if node.right:

                queue.append(node.right)

        # after the current for loop ends place node value of all level in global array
        tree.append(level)

    return tree


#            1
#       2          3
#    4     5    6      7
#

d=TreeNode(4,None,None)
e=TreeNode(5,None,None)
f=TreeNode(6,None,None)
g=TreeNode(7,None,None)

b=TreeNode(2,d,e)
c=TreeNode(3,f,g)

a=TreeNode(1,b,c)

tree=bfs(a)

for level in tree:
    print(level)
    print()

        

            






                





    






               



           
    

            

   







    






















    


        


