from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head:Optional[ListNode]):

    if head == None:
        return False
    
    nodes = set()

    while head.next != None:

        if head in nodes:
            return True
        
        else:
            # we add the whole node instead of just the value because nodes may have the same values but not the same neighboors
            nodes.add(head)
            head = head.next

    return False



a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

a.next = b
b.next = c
c.next = d
d.next = b

print(hasCycle(a))
print()

a = ListNode(1)
b = ListNode(2)

a.next = b
b.next = a

print(hasCycle(a))
print()

a = ListNode(1)

print(hasCycle(a))
print()

