# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ptr = head
        prev = None
        while ptr is not None:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        return ptr
