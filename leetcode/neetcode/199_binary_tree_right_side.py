from tree_helper import *
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        queue = deque()
        queue.append((0, root))
        res = []
        temp = []
        level = 0
        while queue:
            l, node = queue.popleft()
            if level != l:
                res.append(temp[-1])
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
    print(sol.rightSideView(root))

if __name__ == '__main__':
    root = [1,2,3,None,5,None,4]
    test(root)
    root = [1,2,3,4,None,None,None,5]
    test(root)