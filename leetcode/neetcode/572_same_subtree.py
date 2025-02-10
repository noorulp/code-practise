from tree_helper import *
from collections import deque

class Solution:
    
    def traversal(self, node: TreeNode):
        if node is None:
            return '$'
        l = self.traversal(node.left)
        r = self.traversal(node.right)
        s = str(node.val)  + l + r
        return s
    
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        sub = self.traversal(subRoot)
        hashSubRoot = hash(sub)
        found = False
        
        def dfs(node: TreeNode) -> str:
            nonlocal found
            nonlocal hashSubRoot
            if node is None or found:
                return '$'
            l = dfs(node.left)
            r = dfs(node.right)
            s = str(node.val) + l + r
            hashVal = hash(s)
            if hashVal == hashSubRoot:
                found = True
            return s
        
        dfs(root)
        return found


def test(root: list, subRoot: list):
    r = createTreeFromArray(root)
    sr = createTreeFromArray(subRoot)
    sol = Solution()
    print(sol.isSubTree(r, sr))

if __name__ == '__main__':
    root = [3,4,5,1,2]
    subRoot = [4,1,2]
    test(root, subRoot)
    root = [3,4,5,1,2,None,None,None,None,0]
    subRoot = [4,1,2]
    test(root, subRoot)