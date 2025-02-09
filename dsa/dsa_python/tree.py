from collections import deque

class TreeNode:
    def __init__(self, val: int, lchild = None, rchild = None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

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
    root.lchild = one
    root.rchild = two
    one.lchild = thr
    one.rchild = fr
    two.lchild = fv
    two.rchild = sx
    sx.rchild = sv
    return root

def createTreeFromArray(arr: list) -> TreeNode:
    n = len(arr)
    def create(index: int):
        if index >= n:
            return None
        node = TreeNode(arr[index])
        node.lchild = create(2 * index + 1)
        node.rchild = create(2 * index + 2)
        return node
    root = create(0)
    return root


def printLeafNodes(root: TreeNode) -> None:

    res =[]
    def findLeaf(node: TreeNode):
        if node.lchild is None and node.rchild is None:
            res.append(node)
            return
        if node.lchild:
            findLeaf(node.lchild)
        if node.rchild:
            findLeaf(node.rchild)

    findLeaf(root)
    for node in res:
        print(node.val, end= ' ')
    print()  

def inorderTraversal(root: TreeNode) -> None:

    def inorder(node: TreeNode):
        if node is None:
            return
        inorder(node.lchild)
        print(node.val, end= ' ')
        inorder(node.rchild)
    inorder(root)

def bfs(root: TreeNode, num: int) -> bool:
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.val, end= ' ')
        if node.val == num:
            return True
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)
    return False

def dfs(root: TreeNode, num: int) -> bool:

    def search(node: TreeNode):
        if node is None:
            return False
        print(node.val, end= ' ')
        if node.val == num:
            return True
        return search(node.lchild) or search(node.rchild)
    return search(root)

if __name__ == '__main__':
    root = createTree()
    print(dfs(root, 7))
    print(bfs(root, 10))
    arr = [0,1,2,3,4,5,6,7,8]
    root2 = createTreeFromArray(arr)
    inorderTraversal(root2)
    