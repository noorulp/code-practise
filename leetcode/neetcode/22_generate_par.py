from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        output = []
        def generate(s: str, i: int, j: int):
            if i == 0 or i == j:
                s += '('
                generate(s,i+1,j)
            elif i == n:
                while j < n:
                    j += 1
                    s += ')'
                print(s)
                output.append(s)
            elif i > j:
                generate(s+'(',i+1,j)
                generate(s+')',i,j+1)

        generate("",0,0)
        return output

if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(4))