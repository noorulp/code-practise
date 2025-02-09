from tree_helper import *
from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

if __name__ == '__main__':
    arr = [0,1,2,3,4,None,6,7,8]
    root = createTreeFromArray(arr)
    printTree(root)
    sol = Solution()
    print(sol.maxDepth(root))