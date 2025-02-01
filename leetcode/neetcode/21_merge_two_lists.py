# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        ptr = ListNode()
        head = ptr
        while list1 is not None or list2 is not None:
            if list1 is None:
                ptr.next = list2
                list2 = list2.next
            elif list2 is None:
                ptr.next = list1
                list1 = list1.next
            elif list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        return head.next
    

if __name__ == '__main__':
    list1 = [1,2,3,4]
    list2 = [1,3,5,7]
    head1 = ListNode()
    head2 = ListNode()
    ptr1 = head1
    ptr2 = head2
    for val in list1:
        node = ListNode(val)
        ptr1.next = node
        ptr1 = ptr1.next
    for val in list2:
        node = ListNode(val)
        ptr2.next = node
        ptr2 = ptr2.next
    
    ptr1 = head1
    while ptr1 is not None:
        print(ptr1.val)
        ptr1 = ptr1.next
    ptr2 = head2
    while ptr2 is not None:
        print(ptr2.val)
        ptr2 = ptr2.next
    print("Solution")
    sol = Solution()
    h3 = sol.mergeTwoLists(head1.next, head2.next)
    ptr3 = h3
    while ptr3 is not None:
        print(ptr3.val)
        ptr3 = ptr3.next