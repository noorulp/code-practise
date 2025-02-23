from collections import deque
from tree_helper import *


class TreeNode:
    def __init__(self, val = 0, left =None, right =None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        stack = deque()
        root = TreeNode(preorder[0])
        stack.append(root)
        preI = 1
        l = 0
        while stack:
            if stack[-1].val == postorder[l]:
                stack.pop()
                l += 1
            else:
                node = TreeNode(preorder[preI])
                if stack[-1].left == None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
                stack.append(node)
                preI += 1
        return root


def test(preorder: list, postorder: list):
    sol = Solution()
    root = sol.constructFromPrePost(preorder, postorder)
    printTree(root)

if __name__ == '__main__':
    test(preorder = [1,2,4,5,6,7,3], postorder = [4,6,7,5,2,3,1])