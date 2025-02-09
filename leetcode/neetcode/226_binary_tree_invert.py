from tree_helper import *
from collections import deque

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            # swap l and r
            if node:
                temp = node.left
                node.left = node.right
                node.right = temp
                queue.append(node.left)
                queue.append(node.right)
        return root


if __name__ == '__main__':
    arr = [0,1,2,3,4,5,6,7,8]
    root = createTreeFromArray(arr)
    printTree(root)
    sol = Solution()
    nroot = sol.invertTree(root)
    printTree(nroot)