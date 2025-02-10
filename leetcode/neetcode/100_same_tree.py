from tree_helper import *

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def test(p: list, q: list):
    rootp = createTreeFromArray(p)
    rootq = createTreeFromArray(q)
    sol = Solution()
    print(sol.isSameTree(rootp, rootq))

if __name__ == '__main__':
    p = [1,2,3]
    q = [1,2,3]
    test(p, q)
    p = [1,2]
    q = [1,None,2]
    test(p, q)
    p = [1,2,1]
    q = [1,1,2]
    test(p, q)