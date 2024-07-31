class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def maxDepth(root:Node | None):

    if root == None:
        return 0
    
    # reset children's max depth to 0 at every level
    depth = 0
    if root.children is not None:
        # if current child has deeper depth than replace depth with it
        # check all children
        for child in root.children:
            depth = max(depth, maxDepth(child))

    # max children's depth + itself
    return depth + 1



a5 = Node(5,None)
a6 = Node(6,None)

a3 = Node(3,[ a5, a6 ])
a2 = Node(2,None)
a4 = Node(4,None)

a1 = Node(1,[ a3, a2, a4 ])

print("ans",maxDepth(a1))

