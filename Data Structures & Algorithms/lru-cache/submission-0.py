class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        nxt, prev = node.next, node.prev
        nxt.prev = prev
        prev.next = nxt
    
    def insert(self, node):
        nxt, prev = self.right, self.right.prev
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            self.insert(self.hashMap[key])
            return self.hashMap[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
        self.hashMap[key] = Node(key, value)
        self.insert(self.hashMap[key])

        if len(self.hashMap) > self.capacity:
            removedNode = self.left.next
            self.remove(removedNode)
            del self.hashMap[removedNode.key]

