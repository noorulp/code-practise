from tree import *

class BinarySearchTree:
    def checkForBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left:
            if root.left.val > root.val:
                return False
        if root.right:
            if root.right.val < root.val:
                return False
        return self.checkForBST(root.left) and self.checkForBST(root.right)
    
    def insert(self, root: TreeNode, key: int):
        if root is None:
            return TreeNode(key)
        if key > root.val:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)
        return root
    

    def inorderSuccessor(self, node: TreeNode) -> TreeNode:
        '''
        finds the inorder successor of node
        i.e the element that appears just after the given node in inorder traversal of a binary tree
        i.e the leftmost element to the node
        '''
        node = node.right
        while node and node.left:
            node = node.left
        return node

    def delete(self, root: TreeNode, key: int) -> bool:
        if root is None:
            return None
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            # key == val
            if root.right is None:
                # no right node
                root = root.left
            elif root.left is None:
                # no left node
                root = root.right
            else:
                # has both nodes
                succ = self.inorderSuccessor(root)
                root.val = succ.val
                root.right = self.delete(root.right, succ.val)
        return root


def testCheck():
    arr = [2, 1, 5, None, None, 3, 7]
    root = createTreeFromArray(arr)
    printTree(root)
    bst = BinarySearchTree()
    print(bst.checkForBST(root))

def testInsert():
    arr = [2, 1, 5, None, None, 3, 7]
    root = createTreeFromArray(arr)
    bst = BinarySearchTree()
    bst.insert(root, -1)
    printTree(root)
    bst.insert(root, 4)
    printTree(root)
    bst.insert(root, 6)
    printTree(root)

def testDelete():
    bst = BinarySearchTree()
    arr = [100, 50, 40, 80, 30, 45, 60, 90, 70]
    root = None
    for num in arr:
        root = bst.insert(root, num)
    printTree(root)
    root = bst.delete(root, 50)
    printTree(root)

if __name__ == '__main__':
    testDelete()