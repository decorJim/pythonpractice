
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    
    def dfs(root: Optional[TreeNode], sum: int):

        # test if the initial node is Null
        if root == None:
            return False

        sum += root.val

        # will evaluate if expression is True or False and return the value
        if not root.left and not root.right:
            return sum == targetSum
        
        # if either one returns True the whole expression is True
        # is done at each path split in tree
        return dfs(root.right, sum) or dfs(root.left, sum)

    return dfs(root, 0)


n4_7 = TreeNode(7, None, None)
n4_2 = TreeNode(2, None, None)
n4_1 = TreeNode(1, None, None)

n3_11 = TreeNode(11, n4_7, n4_2)
n3_13 = TreeNode(13, None, None)
n3_4 = TreeNode(4, None, n4_1)

n2_4 = TreeNode(4, n3_11, None)
n2_8 = TreeNode(8, n3_13, n3_4)

n1_5 = TreeNode(5, n2_4, n2_8)

print(hasPathSum(n1_5, 22))
print()

n2_2 = TreeNode(2, None, None)
n2_3 = TreeNode(3, None, None)

n1_1 = TreeNode(1, n2_2, n2_3)

print(hasPathSum(n1_1, 5))
print()


print(hasPathSum(None, 0))
print()


        



