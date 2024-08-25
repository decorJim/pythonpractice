import heapq
from typing import List

class ListNode:

    def __init__(self, val, next):
        self.val = val
        self.next = next


def mergeKSoretdLists(lists: List[ListNode]):

    queue = []

    # we have to use i values loop because inserting into a heap 
    # sorts element according to keys so if there is 2 identical 
    # keys object cant be compared
    # i is to make sure if 2 differents lists have same node values
    # we can differentiate them
    for i in range(len(lists)):

        list = lists[i]

        # this value is to make sure we can differentiate 2 nodes with 
        # same value in the same linked list
        counter = 0

        while list != None:

            heapq.heappush(queue, (list.val, i, counter, list))
            list = list.next

    
    val, i, counter, firstNode = heapq.heappop(queue)

    # keep tracks of the last element to link it to the current one
    stack = [firstNode]

    while queue:

        previous = stack.pop()
        val, i, counter, node = heapq.heappop(queue)
        previous.next = node
        stack.append(node)

    return firstNode

list1_5 = ListNode(5, None)
list1_4 = ListNode(4, list1_5)
list1_1 = ListNode(1, list1_4)

list2_4 = ListNode(4, None)
list2_3 = ListNode(3, list2_4)
list2_1 = ListNode(1, list2_3)

list3_6 = ListNode(6, None)
list3_2 = ListNode(2, list3_6)

node = mergeKSoretdLists([list1_1, list2_1, list3_2])
while node != None:
    print(node.val)
    print()
    node = node.next
print("-------------------")

        

        

        