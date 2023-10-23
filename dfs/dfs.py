#  DFS template
#  start with defining the quitting condition once a leaf node child is reached
#  do something to the current node
#  recursive call all of its children
#  return current node after each call

from typing import Optional


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

order=[]

def dfs(root:Optional[TreeNode]):

    # put the quitting condition after reaching a leaf node children
    if root==None:
       return 
    
    # do something in the current node
    order.append(root.val)

    # call childrens if more than 2 use a for loop
    # recursive call on childrens
    if root.left:
       dfs(root.left)

    if root.right:
       dfs(root.right)

    # each node will return himself to the previous call until root node
    # return root is confusing but normally it should be return node
    return root


#         1
#     2       3
#  4    5   6    7
#

d=TreeNode(4,None,None)
e=TreeNode(5,None,None)
f=TreeNode(6,None,None)
g=TreeNode(7,None,None)

b=TreeNode(2,d,e)
c=TreeNode(3,f,g)

a=TreeNode(1,b,c)

dfs(a)

print(order)



        

            






                





    






               



           
    

            

   







    






















    


        


