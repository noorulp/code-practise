# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = 0
        fast = head
        curr = head
        prev = None
        while i < n:
            fast = fast.next
            i += 1
        
        while fast != None:
            fast = fast.next
            prev = curr
            curr = curr.next
        
        if prev != None:
            prev.next = curr.next
            return head
        else:
            return curr.next

    def print(self, head: ListNode):
        while head != None:
            print(head.val)
            head = head.next

if __name__ == '__main__':
    list = [1,2,3]
    n = 3
    head = ListNode()
    ptr1 = head
    for val in list:
        node = ListNode(val)
        ptr1.next = node
        ptr1 = ptr1.next
    n = 1

    sol = Solution()
    head = sol.removeNthFromEnd(head, n)
    sol.print(head)