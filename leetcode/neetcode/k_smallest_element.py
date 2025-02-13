from tree_helper import *
from collections import deque

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # inorder traversal
        index = 1
        stack = deque()
        node = root
        while node:
            stack.append(node)
            node = node.left
        while stack:
            node = stack.pop()
            if node:
                if index == k:
                    return node.val
                index += 1
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return 0

    def inorder(self, node: TreeNode):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val, end= ' ')
        self.inorder(node.right)
    
def test(arr: list, k: int):
    root = createTreeFromArray(arr)
    sol = Solution()
    sol.inorder(root)
    print()
    print(sol.kthSmallest(root, k))


if __name__ == '__main__':
    test(arr = [30, 10, 40, None, 20, None, None, None, None, 15, 25], k = 3)
    test(arr = [3,1,4,None,2], k = 1)
    test(arr = [5,3,6,2,4,None,None,1], k = 3)