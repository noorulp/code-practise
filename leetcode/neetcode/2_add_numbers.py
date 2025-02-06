# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = l1
        head2 = l2
        sum = 0
        carryover = 0
        head3 = ListNode()
        ans = head3
        while head1 or head2:
            if head1 is None:
                num = head2.val
                head2 = head2.next
            elif head2 is None:
                num = head1.val
                head1 = head1.next
            else:
                num = head1.val + head2.val
                head1 = head1.next
                head2 = head2.next
            num += carryover
            carryover = int(num / 10)
            node = ListNode()
            node.val = num % 10
            head3.next = node
            head3 = head3.next
            sum += (num % 10)
        if carryover == 1:
            node = ListNode(carryover)
            head3.next = node
        
        return ans.next
