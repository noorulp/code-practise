from tree_helper import *

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        balanced = True
        def depth(node: TreeNode) -> int:
            nonlocal balanced
            if node is None or not balanced:
                return 0
            dl = depth(node.left)
            dr = depth(node.right)
            if max(dl, dr) - min(dl, dr) > 1:
                balanced = False
            return 1 + max(dl, dr)
        depth(root)
        return balanced

def test(arr: list):
    sol = Solution()
    root = createTreeFromArray(arr)
    print(sol.isBalanced(root))

if __name__ == '__main__':
    root = [3,9,20,None,None,15,7]
    test(root)
    root = [1,2,2,3,3,None,None,4,4]
    test(root)
    root = []
    test(root)