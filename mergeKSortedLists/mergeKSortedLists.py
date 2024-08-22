from typing import List


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def mergeKSortedLists(lists:List[ListNode]):

    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:

        mergedLists = []

        # merge 2 linked list every time so advance by 2
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            # if length is odd number the last l2 might be null
            l2 = lists[ i + 1 ] if (i + 1) < len(lists) else None

            mergedList = mergeList(l1, l2)
            mergedLists.append(mergedList)

        lists = mergedLists

    return lists[0]



def mergeList(l1:ListNode, l2:ListNode):

    dummy = ListNode()

    it = dummy

    while l1 and l2:

        if l1.val < l2.val:

            it.next = l1
            l1 = l1.next

        else:

            it.next = l2
            l2 = l2.next

        it = it.next

    if l1:
        it.next = l1

    elif l2:
        it.next = l2

    return dummy.next

list1_5 = ListNode(5, None)
list1_4 = ListNode(4, list1_5)
list1_1 = ListNode(1, list1_4)

list2_4 = ListNode(4, None)
list2_3 = ListNode(3, list2_4)
list2_1 = ListNode(1, list2_3)

list3_6 = ListNode(6, None)
list3_2 = ListNode(2, list3_6)


node = mergeKSortedLists([list1_1, list2_1, list3_2])
while node != None:
    print(node.val)
    print()
    node = node.next
print("-------------------")



