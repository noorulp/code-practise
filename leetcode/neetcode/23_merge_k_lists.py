import heapq

class ListNode:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        head = ListNode()
        ptr = head
        prev = head
        k = len(lists)
        heapnodes = []
        for node in lists:
            if node:
                heapnodes.append((node.val, node))
        heapq.heapify(heapnodes)
        while len(heapnodes) > 0:
            # pop the smallest
            val, node = heapq.heappop(heapnodes)
            if node.next:
                heapq.heappush(heapnodes, (node.next.val, node.next))
            ptr.next = node
            ptr = node
        return head.next

if __name__ == '__main__':
    lists = [[2,3],[1,15],[9,10]]
    ptrs = []
    for nums in lists:
        head = ListNode()
        ptr = head
        for num in nums:
            node = ListNode(num)
            ptr.next = node
            ptr = ptr.next
        ptrs.append(head.next)
    sol = Solution()
    ptr = sol.mergeKLists(ptrs)
    while ptr is not None:
        print(f'{ptr.val}->', end= ' ')
        ptr = ptr.next