from collections import deque
import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque()
        for token in tokens:
            if token == '+':
                val = stack.pop() + stack.pop()
            elif token == '-':
                val = stack.pop()
                val = stack.pop() - val
            elif token == '/':
                val = stack.pop()
                val = int(stack.pop()/val)     
            elif token == '*':
                val = stack.pop() * stack.pop()        
            else:
                val = int(token)
            stack.append(val)
        return stack.pop()

if __name__ == '__main__':
    sol = Solution()
    #tokens = ["2","1","+","3","*"]
    #print(sol.evalRPN(tokens))
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN(tokens))