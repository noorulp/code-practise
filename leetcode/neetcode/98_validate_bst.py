from tree_helper import *
from collections import deque

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nodes = []
        def inorder(node: TreeNode) -> list:
            if node is None:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        inorder(root)
        n = len(nodes)
        i = 1
        while i < n:
            if nodes[i-1] >= nodes[i]:
                return False
            i += 1
        return True
    
def test(arr: list):
    root = createTreeFromArray(arr)
    sol = Solution()
    print(sol.isValidBST(root))

if __name__ == '__main__':
    root = [2,1,3]
    test(root)
    root = [5,1,4,None,None,3,6]
    test(root)
    root = [5,4,6,None,None,3,7]
    test(root)