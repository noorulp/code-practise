from collections import deque

class TreeNode:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def createTree() -> TreeNode:
    """
    creates a tree like so:
                0
            1       2
           3 4     5  6
                       7
    """
    root = TreeNode(0)
    one = TreeNode(1)
    two = TreeNode(2)
    thr = TreeNode(3)
    fr = TreeNode(4)
    fv = TreeNode(5)
    sx = TreeNode(6)
    sv = TreeNode(7)
    root.left = one
    root.right = two
    one.left = thr
    one.right = fr
    two.left = fv
    two.right = sx
    sx.right = sv
    return root

def createTreeFromArray(arr: list) -> TreeNode:
    n = len(arr)
    def create(index: int):
        if index >= n:
            return None
        if arr[index] is None:
            return None
        node = TreeNode(arr[index])
        node.left = create(2 * index + 1)
        node.right = create(2 * index + 2)
        return node
    root = create(0)
    return root


def printLeafNodes(root: TreeNode) -> None:

    res =[]
    def findLeaf(node: TreeNode):
        if node.left is None and node.right is None:
            res.append(node)
            return
        if node.left:
            findLeaf(node.left)
        if node.right:
            findLeaf(node.right)

    findLeaf(root)
    for node in res:
        print(node.val, end= ' ')
    print()  

def inorderTraversal(root: TreeNode) -> None:

    def inorder(node: TreeNode):
        if node is None:
            return
        inorder(node.left)
        print(node.val, end= ' ')
        inorder(node.right)
    inorder(root)

def bfs(root: TreeNode, num: int) -> bool:
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.val, end= ' ')
        if node.val == num:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return False

def dfs(root: TreeNode, num: int) -> bool:

    def search(node: TreeNode):
        if node is None:
            return False
        print(node.val, end= ' ')
        if node.val == num:
            return True
        return search(node.left) or search(node.right)
    return search(root)

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
                    print('x', end= ' ')
                else:
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
        

if __name__ == '__main__':
    root = createTree()
    print(dfs(root, 7))
    print(bfs(root, 10))
    arr = [0,1,2,3,4,5,6,7,8]
    root2 = createTreeFromArray(arr)
    inorderTraversal(root2)
    print()
    printTree(root2)
    