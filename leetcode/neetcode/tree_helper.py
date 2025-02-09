# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTreeFromArray(arr: list) -> TreeNode:
    n = len(arr)
    def create(index: int):
        if index >= n:
            return None
        node = TreeNode(arr[index])
        node.left = create(2 * index + 1)
        node.right = create(2 * index + 2)
        return node
    root = create(0)
    return root
