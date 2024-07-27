from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head:Optional[ListNode]):

    fast = head
    slow = head


    # condition is to make sure we can perform .next.next
    # if A -> None then we cannot call None.next even as the while condition it will not be supported
    # fast will finish before slow if there is no cycle so no need to verify slow
    while fast and fast.next:

        print("slow", slow.val)
        print("fast", fast.val)

        # move slow by one
        slow = slow.next

        # move fast by two
        fast = fast.next.next

        # if they meet again then there is a cycle
        if fast == slow:
            print()
            print("SAME NODE")
            print("slow", slow.val)
            print("fast", fast.val)
            print()
            return True
        
        print("----------------")

        
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
print("---------------------------------------------")

a = ListNode(1)
b = ListNode(2)

a.next = b
b.next = a

print(hasCycle(a))
print("---------------------------------------------")

a = ListNode(1)

print(hasCycle(a))
print("---------------------------------------------")
