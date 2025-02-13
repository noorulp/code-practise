from tree_helper import *

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        maxSum = -1001

        def pathSum(node: TreeNode) -> int:
            nonlocal maxSum
            l = r = 0
            if node.left:
                l = pathSum(node.left)
            if node.right:
                r = pathSum(node.right)
            maxSum = max(maxSum, node.val, l + node.val, r + node.val, l + r + node.val)
            return max(l + node.val, r + node.val, node.val)

        sum = pathSum(root)
        return maxSum

def test(arr: list):
    root = createTreeFromArray(arr)
    printTree(root)
    sol = Solution()
    print(sol.maxPathSum(root))

if __name__ == '__main__':
    root = [-10,9,20,None,None,15,7]
    #test(root)
    test(arr= [3,9,20,11,12,15,7])