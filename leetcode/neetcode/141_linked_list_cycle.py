class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow_ptr = head
        fast_ptr = head
        found = False
        while slow_ptr is not None and fast_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
            if fast_ptr is not None:
                fast_ptr = fast_ptr.next
            if slow_ptr == fast_ptr:
                found = True
                break

        if not found:
            return -1
        
        index = 0
        while head != slow_ptr:
            head = head.next
            index += 1        
        return index
    

if __name__ == '__main__':
    #head = ListNode(3)
    print(type(chr(97)))