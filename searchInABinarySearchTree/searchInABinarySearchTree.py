

from typing import Optional


class TreeNode:

    def __init__(self, val = 0, left = None, right = None):

        self.val = val
        self.left = left
        self.right = right

def searchBST(root: Optional[TreeNode], val: int):

    if root == None:
        return None
    
    elif root.val == val:
        return root
    
    if val < root.val:
        return searchBST(root.left, val)
    
    else:
        return searchBST(root.right, val)
    


l3_n1 = TreeNode(1, None, None)
l3_n3 = TreeNode(3, None, None)

l2_n2 = TreeNode(2, l3_n1, l3_n3)
l2_n7 = TreeNode(7, None, None)

l1_n4 = TreeNode(4, l2_n2, l2_n7)

print(searchBST(l1_n4, 2).val)
print()

print(searchBST(l1_n4, 5))
print()
        