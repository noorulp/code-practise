from tree_helper import *

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        res = root
        while True:
            # case 1 : both values are greater than node
            if p.val > res.val and q.val > res.val:
                res = res.right
            # case 2 : both values are lower than node
            elif p.val < res.val and q.val < res.val:
                res = res.left
            # case 3 : node is in range [p, q]
            else:
                break
        return res


def test(arr: list, p: int, q: int):
    root = createTreeFromArray(arr)
    pr = search(root, p)
    qr = search(root, q)
    sol = Solution()
    print(sol.lowestCommonAncestor(root, pr, qr).val)
if __name__ == '__main__':
    root = [6,2,8,0,4,7,9,None,None,3,5]
    p = 2
    q = 8
    test(root, p, q)
    test(root, 2, 4)
    test(root, 6, 9)