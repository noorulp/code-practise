from tree_helper import *
from collections import deque

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ''
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node:
                res = res + str(node) + '#'
                queue.append(node.left)
                queue.append(node.right)
            else:
                res = res + '$' + '#'


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

def test(arr:list):
    

if __name__ == '__main__':
    s = '#'
    l = s.split('#')
    print(l)