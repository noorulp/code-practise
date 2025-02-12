from tree_helper import *
from collections import deque

class Solution:

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        pass




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

if __name__ == '__main__':
    #sample(arr= [3,9,20,11,12,15,7])
    sample(arr= [3,9,None,11,12,None,None,None,14,None,13,None,None,None,None,None,None,1,2])
    #test(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
    #test(preorder = [-1], inorder = [-1])