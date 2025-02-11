from tree_helper import *
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        queue = deque()
        queue.append((0, root))
        res = []
        temp = []
        level = 0
        while queue:
            l, node = queue.popleft()
            if level != l:
                res.append(temp)
                temp = []
                level = l
            if node:
                temp.append(node.val)
                queue.append((l+1, node.left))
                queue.append((l+1, node.right))
        
        return res     

def test(arr: list):
    root = createTreeFromArray(arr)
    sol = Solution()
    print(sol.levelOrder(root))

if __name__ == '__main__':
    root = [3,9,20,None,None,15,7]
    test(root)
    test([0])
    test([])
