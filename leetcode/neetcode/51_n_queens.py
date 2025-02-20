
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.'] * n for _ in range(0, n)]
        res = []
        # a board will have n rows and n columns
        # a board will have 2 *  2n - 1 diagonals
        # one that cuts through center is i = j
        # others along the row are 0 < i - j < n
        # others along the column are 0 < j - i < n
        # the same for diagonals where i + j = same number
        # queen at (i, j) blocks i row, j column, i - j diagonal and i + j diagonal
        def placeQueen(row: int, blockedCol: set, blockedAdd: set, blockedSub: set):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for col in range(0, n):
                if col in blockedCol or (row - col) in blockedSub or (row + col) in blockedAdd:
                    continue
                # add
                board[row][col] = 'Q'
                blockedCol.add(col)
                blockedSub.add(row - col)
                blockedAdd.add(row + col)
                placeQueen(row + 1, blockedCol, blockedAdd, blockedSub)
                # remove
                board[row][col] = '.'
                blockedCol.remove(col)
                blockedSub.remove(row - col)
                blockedAdd.remove(row + col)

        placeQueen(0, set(), set(), set())
        return res
    
def test(n: int):
    sol = Solution()
    print(sol.solveNQueens(n))

if __name__ == '__main__':
    test(3)