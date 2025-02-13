from tree_helper import *
from collections import deque

class Solution:

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        hashPre = {}
        hashIn = {}
        for i, (np, ni) in enumerate(zip(preorder, inorder)):
            hashPre[np] = i
            hashIn[ni] = i
        
        preIndex = 0
        n = len(preorder)
        def buildNode(l: int, r: int) -> TreeNode:
            nonlocal hashIn, preIndex, n
            if l > r or preIndex > n:
                return None
            val = preorder[preIndex]
            inIndex = hashIn[val]
            if inIndex < l or inIndex > r:
                # value not found in range
                return None
            # valid range
            preIndex += 1
            node = TreeNode(val)
            node.left = buildNode(l, inIndex - 1)
            node.right = buildNode(inIndex + 1, r)
            return node
        
        root = buildNode(0, n - 1)
        return root
        

def test(preorder: list[int], inorder: list[int]):
    sol = Solution()
    root = sol.buildTree(preorder, inorder)
    printTree(root)

def sample(arr: list):
    root = createTreeFromArray(arr)
    printTree(root)
    print()
    preorder(root)
    print()
    inorder(root)
    print()

if __name__ == '__main__':
    #sample(arr= [3,9,20,11,12,15,7])
    #sample(arr= [3,9,None,11,12,None,None,None,14,None,13,None,None,None,None,None,None,1,2])
    #test(preorder= [3,9,11,12,20,15,7], inorder= [11,9,12,3,15,20,7])
    #test(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
    test(preorder = [-1], inorder = [-1])