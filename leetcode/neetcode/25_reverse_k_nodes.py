# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(ptr: ListNode):
    while ptr is not None:
        print(f'{ptr.val}->', end= ' ')
        ptr = ptr.next
    print()

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        l = head
        right = head
        newhead = None
        i = 1
        trail = None
        while right.next:
            right = right.next
            i = i + 1
            if i % k == 0:
                left = l
                last = right.next
                prev = last
                while l != last:
                    temp = l.next
                    l.next = prev
                    prev = l
                    l = temp
                if trail:
                    trail.next = prev
                trail = left
                if newhead is None:
                    newhead = right
                printList(newhead)
                right = left

        if newhead:
            return newhead
        return head


if __name__ == '__main__':
    lists = [1,2,3,4,5,6]
    k = 3
    head = ListNode()
    ptr = head
    for val in lists:
        node = ListNode(val)
        ptr.next = node
        ptr = ptr.next
    head = head.next
    sol = Solution()
    ptr = sol.reverseKGroup(head, k)
    printList(ptr)