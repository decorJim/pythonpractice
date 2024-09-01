
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:

    allSum = set()
    if root == None:
        return False

    def bfs(root: Optional[TreeNode], sum):
        # at each new level we add the node's value to the current sum
        sum += root.val

        # when reaching a leaf node
        if root.left == None and root.right == None:
            # add the sum of the path to the set
            allSum.add(sum)
            return
        
        if root.left:
            bfs(root.left, sum)

        if root.right:
            bfs(root.right, sum)

    bfs(root, 0)
    
    print(allSum)

    # if the sum is the set return True
    if targetSum in allSum:
        return True
    else:
        return False
    


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


        



