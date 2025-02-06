class Node:
    def __init__(self, key: int, value: int):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node: Node):
        # insert at front, just after head
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        node = self.dict.get(key, None)
        if node is None:
            return -1
        # remove node
        self.remove(node)
        # add to front
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.dict.get(key, None)
        if node is not None:
            node.value = value
            self.get(key)
            return
        node = Node(key, value)
        if self.size == 0:
            self.head.next = node
            node.prev = self.head
            node.next = self.tail
            self.tail.prev = node
            self.size = 1
        elif self.size == self.capacity:
            tail = self.tail.prev
            self.insert(node)
            self.remove(self.tail.prev)
            self.dict.pop(tail.key)
        else:
            self.size = self.size + 1
            self.insert(node)
        self.dict[key] = node
    
    def print(self):
        ptr = self.head
        while ptr:
            print(f'{ptr.key}: {ptr.value} ->', end= ' ')
            ptr = ptr.next
        print(' ')

if __name__ == '__main__':

    actions = ["put","put","get","put","put","get"]
    inputs = [[2,1],[2,2],[2],[1,1],[4,1],[2]]
    obj = LRUCache(capacity= 2)
    for action, input in zip(actions, inputs):
        if action == 'put':
            obj.put(input[0], input[1])
            obj.print()
        elif action == 'get':
            print(obj.get(input[0]))
            obj.print()
    
    actions = ["put","put","get","put","get","put","get","get","get"]
    inputs = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    obj = LRUCache(capacity= 2)
    for action, input in zip(actions, inputs):
        if action == 'put':
            obj.put(input[0], input[1])
            obj.print()
        elif action == 'get':
            print(obj.get(input[0]))
    