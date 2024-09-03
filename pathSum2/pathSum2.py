
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    
    ans = []

    # variables like list in python are passed as reference so modifications affects the original
    def dfs(root: Optional[TreeNode], path: List[int], sum: int):

        sum += root.val

        # adds new element to array as a copy
        # we dont just use append because 
        # by reference seperate calls will modify the original
        tmp = path + [root.val]

        # the tmp array will just dissappear if the sum is not the target
        if not root.left and not root.right and sum == targetSum:
            ans.append(tmp)

        if root.left:
            dfs(root.left, tmp, sum)

        if root.right:
            dfs(root.right, tmp, sum)

    
    dfs(root, [], 0)

    return ans

        

n4_7 = TreeNode(7, None, None)
n4_2 = TreeNode(2, None, None)
n4_5 = TreeNode(5, None, None)
n4_1 = TreeNode(1, None, None)

n3_11 = TreeNode(11, n4_7, n4_2)
n3_13 = TreeNode(13, None, None)
n3_4 = TreeNode(4, n4_5, n4_1)

n2_4 = TreeNode(4, n3_11, None)
n2_8 = TreeNode(8, n3_13, n3_4)

n1_5 = TreeNode(5, n2_4, n2_8)

print(pathSum(n1_5, 22))
print()

n2_2 = TreeNode(2, None, None)
n2_3 = TreeNode(3, None, None)

n1_1 = TreeNode(1, n2_2, n2_3)

print(pathSum(n1_1, 5))
print()

n2_2 = TreeNode(2, None, None)

n1_1 = TreeNode(1, n2_2, None)

print(pathSum(n1_1, 0))
print()


    

