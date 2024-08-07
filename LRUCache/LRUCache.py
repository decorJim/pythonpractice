class Node:

    def __init__(self, key:int, value:int) -> None:
        
        self.key = key
        self.value = value
        
        self.prev = None
        self.next = None


class Cache:

    def __init__(self, capacity:int) -> None:
        
        self.capacity = capacity
        
        # using hashmap allows get and put operations to be O(1)
        self.cache = {}
        
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

        # initial pointers's state
        #   left       right
        #     |         |
        #   Node(0) -> Node(0)  
        #           <-


    # remove a node from the linked list at any place
    def remove(self, node:Node) -> None:
        
        previous = node.prev
        next = node.next

        #  remove Node(2)
        #
        #  Node(1) -> Node(2) -> Node(3)
        #          <-         <-

        # change pointer of the nodes sandwiching the target
        # Node(1) -> Node(3)
        previous.next = next

        # Node(1) <- Node(3)
        next.prev = previous

        # delete the pointer pointing to old node from the hashmap
        del self.cache[node.key]



    # insert node at the right where 
    # most recent accessed node are
    def insert(self, node:Node) -> None:

        # finds most recent node using right pointer's prev
        mostRecentNode = self.right.prev
        mostRecentNode.next = node
        self.right.prev = node

        node.prev = mostRecentNode
        node.next = self.right

        # change pointer in hashmap to point to new node
        self.cache[node.key] = node


    # every time we get a value
    # the value needs to be marked 
    # as the most recent element
    def get(self, key:int) -> int:
        if key in self.cache:
            targetNode = self.cache[key]
            # remove the node from it's current place in the linked list
            self.remove(targetNode)

            # add node to the right side of list as the most recent element
            self.insert(targetNode)
            return targetNode.value
        return -1
    
    def put(self, key:int, value:int) -> None:

        if key in self.cache:
            # remove old node value
            self.remove(self.cache[key])

        # insert new 
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove the least recent node
            leastRecent = self.left.next
            # remove from the linked list
            self.remove(leastRecent)



instructions = ["LRUCache","put","put","get","put","get","put","get","get","get"]
inputs = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

obj = Cache(inputs[0][0])

for i in range(0,len(instructions)):
    if instructions[i] == "get":
        print(obj.get(inputs[i][0]))

    elif instructions[i] == "put":
        obj.put(inputs[i][0], inputs[i][1])
        print("null")

    else:
        print("null")

    

