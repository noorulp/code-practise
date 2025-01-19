import math

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_hashes = [set() for _ in range(9)]
        col_hashes = [set() for _ in range(9)]
        cube_hashes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_hashes[i] or board[i][j] in col_hashes[j] or board[i][j] in cube_hashes[math.floor(i/3)*3 + math.floor(j/3)]:
                    return False
                row_hashes[i].add(board[i][j])
                col_hashes[j].add(board[i][j])
                cube_hashes[math.floor(i/3)*3 + math.floor(j/3)].add(board[i][j])

        return True

if __name__ == '__main__':
    S = Solution()
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(S.isValidSudoku(board))