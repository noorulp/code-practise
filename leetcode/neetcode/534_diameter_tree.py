from tree_helper import *
from collections import deque

class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode)-> int:
        maxcount = 0
        def maxlevel(node: TreeNode, level: int) -> int:
            nonlocal maxcount
            if node is None:
                # found leaf node
                return level - 1
            
            l = maxlevel(node.left, level + 1)
            r = maxlevel(node.right, level + 1)
            d = l - level + r - level
            if d > maxcount:
                maxcount = d
            return max(l, r)
        
        maxlevel(root, 0)
        return maxcount


if __name__ == '__main__':
    arr = [0,1,2,3,4,None,6,7,8]
    root = createTreeFromArray(arr)
    printTree(root)
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))
    arr = [1,2]
    root = createTreeFromArray(arr)
    print(sol.diameterOfBinaryTree(root))