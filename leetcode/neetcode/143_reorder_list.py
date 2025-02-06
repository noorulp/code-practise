
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # for even length, n/2 + 1. for odd length n/2
        if fast:
            slow = slow.next
        endPtr = slow
        # reverse 2nd half
        prev = None
        slow = slow.next
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # attach 2nd half to 1st half
        endPtr.next = prev

        ptr = head
        nptr = prev
        while nptr:
            temp = ptr.next
            temp2 = nptr.next
            ptr.next = nptr
            nptr.next = temp
            nptr = temp2
            ptr = temp
        endPtr.next = None

if __name__ == '__main__':
    list1 = [1,2,3,4,5,6]
    head1 = ListNode()
    ptr1 = head1
    for val in list1:
        node = ListNode(val)
        ptr1.next = node
        ptr1 = ptr1.next
    head1 = head1.next
    sol = Solution()
    sol.reorderList(head1)
    while head1:
        print(head1.val)
        head1 = head1.next