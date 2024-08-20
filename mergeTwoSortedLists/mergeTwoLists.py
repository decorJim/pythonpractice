class ListNode:
    def __init__(self, val = 0, next = None):

        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    # Dummy node to store the answer linked list
    dummy = ListNode()

    # it 
    # 1 - 2 - 5
    # 
    # 1 - 3 - 9 - 10
    #

    # iterator to put element in answer move between 2 lists
    it = dummy

    while l1 and l2:

        if l1.val < l2.val:
            
            it.next = l1
            l1 = l1.next

        else:

            it.next = l2
            l2 = l2.next

        it = it.next

    # if one list is longer than the other
    # since current l1 is already a sub linked list we are attaching the rest
    if l1:
        it.next = l1
 
    elif l2:
        it.next = l2

    return dummy.next

list1_4 = ListNode(4, None)
list1_2 = ListNode(2, list1_4)
list1_1 = ListNode(1, list1_2)

list2_4 = ListNode(4, None)
list2_3 = ListNode(3, list2_4)
list2_1 = ListNode(1, list2_3)

node = mergeTwoLists(list1_1, list2_1)

while node != None:
    print(node.val)
    print("|")
    node = node.next

print()
print("------------------------")
print()

list1_9 = ListNode(9, None)
list1_5 = ListNode(5, list1_9)
list1_4 = ListNode(4, list1_5)
list1_2 = ListNode(2, list1_4)
list1_1 = ListNode(1, list1_2)

list2_4 = ListNode(4, None)
list2_3 = ListNode(3, list2_4)
list2_1 = ListNode(1, list2_3)

node = mergeTwoLists(list1_1, list2_1)
while node != None:
    print(node.val)
    print("|")
    node = node.next


        

        