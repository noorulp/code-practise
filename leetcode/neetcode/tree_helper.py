from collections import deque

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
        if arr[index] is not None:
            node = TreeNode(arr[index])
            node.left = create(2 * index + 1)
            node.right = create(2 * index + 2)
            return node
        else:
            return None

    root = create(0)
    return root

def printTree(root: TreeNode) -> None:
    '''
    prints a tree to make it easier to see its changes
    '''
    queue = deque()
    queue.append((0, root))
    plist = []
    level = 0
    while queue:
        l, node = queue.popleft()
        if l != level:
            print(f'level {level}:', end= ' ')
            for val in plist:
                if val is None:
                    val = 'x'
                print(val, end= ' ')
            level = l
            print()
            plist.clear()
        if node:
            plist.append(node.val)
            queue.append((l + 1, node.left))
            queue.append((l + 1, node.right))
        else:
            plist.append(None)
        