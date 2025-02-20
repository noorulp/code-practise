
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def search(i: int, j: int, index: int) -> bool:
            nonlocal m, n
            if i < 0 or j <  0 or i == m or j == n or board[i][j] == None:
                return False

            if board[i][j] != word[index]:
                return False
            
            if index + 1 == len(word):
                return True

            temp = board[i][j]
            board[i][j] = None
            # found so go up, down left, right
            # up
            if search(i - 1, j, index + 1):
                return True
            # down
            elif search(i + 1, j, index + 1):
                return True
            # left
            elif search(i, j - 1, index + 1):
                return True
            # right
            elif search(i, j + 1, index + 1):
                return True
            board[i][j] = temp
            return False

        for i in range(0, m):
            for j in range(0, n):
                found = search(i, j, 0)
                if found:
                    return True
        return False

def test(board: list[list[str]], word: str):
    sol = Solution()
    print(sol.exist(board, word))

if __name__ == '__main__':
    test(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
