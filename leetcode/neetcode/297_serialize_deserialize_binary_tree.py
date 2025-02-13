from tree_helper import *
from collections import deque

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TureeNode
        :rtype: str
        """
        res = ''
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                res = res + str(node.val) + ','
                stack.append(node.right)
                stack.append(node.left)
            else:
                res = res + 'x' + ','
        return res[0:-1]

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'x':
            return None
        arr = data.split(',')
        N = len(arr)
        stack = deque()
        tstack = deque()
        i = 0
        # place holder nodes
        leftNode = TreeNode()
        rightNode = TreeNode()
        root = TreeNode(int(arr[i]), leftNode, rightNode)
        tstack.append(root)
        stack.append(i + 1)
        i = 1
        while tstack and i < N:
            if arr[i] == 'x':
                if tstack[-1].left == leftNode:
                    tstack[-1].left = None
                else:
                    tstack[-1].right = None
                    tstack.pop()
            else:
                val = int(arr[i])
                node = TreeNode(val, leftNode, rightNode)
                if tstack:
                    if tstack[-1].left == leftNode:
                        tstack[-1].left = node
                    else:
                        tstack[-1].right = node
                        tstack.pop()
                tstack.append(node)
            i += 1
        return root

def test(arr:list):
    root = createTreeFromArray(arr)
    printTree(root)
    sol = Codec()
    data = sol.serialize(root)
    r = sol.deserialize(data)
    printTree(r)

if __name__ == '__main__':
    arr = [10,20,30,None,40,70,None,None,None,50,60,None,90]
    test([])