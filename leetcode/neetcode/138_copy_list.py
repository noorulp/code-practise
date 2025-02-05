# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        hashMap = {}
        hashMap[None] = None
        ptr = head
        while ptr:
            node = Node()
            node.val = ptr.val
            hashMap[ptr] = node
            ptr = ptr.next
        ptr = head
        while ptr:
            hashMap[ptr].next = hashMap[ptr.next]
            hashMap[ptr].random = hashMap[ptr.random]
            ptr = ptr.next
        return hashMap[head]

if __name__ == '__main__':
    list1 = [1,2,3,4,5,6]
    head1 = Node()
    ptr1 = head1
    for val in list1:
        node = Node(val)
        ptr1.next = node
        ptr1 = ptr1.next
    head1 = head1.next
    sol = Solution()
    head2 = sol.copyRandomList(head1)
    while head2:
        print(head2.val)
        head2 = head2.next