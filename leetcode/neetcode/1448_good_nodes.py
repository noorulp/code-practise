from tree_helper import *

class Solution:
    def goodNodes(self, root: TreeNode):
        count = 0
        def dfs(node: TreeNode, maxVal: int) -> None:
            nonlocal count
            if node is None:
                return
            if node.val >= maxVal:
                count += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, maxVal)
                dfs(node.right, maxVal)

        dfs(root, root.val)
        return count

def test(arr: list):
    root = createTreeFromArray(arr)
    sol = Solution()
    print(sol.goodNodes(root))

if __name__ == '__main__':
    root = [3,1,4,3,None,1,5]
    test(root)
    root = [3,3,None,4,2]
    test(root)