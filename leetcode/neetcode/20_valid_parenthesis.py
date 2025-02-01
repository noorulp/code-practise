from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parMap = dict()
        parMap['('] = ')'
        parMap['['] = ']'
        parMap['{'] = '}'
        for par in s:
            if par == '(' or par == '[' or par == '{':
                stack.append(par)
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if not par == parMap[ch]:
                    return False
        if len(stack) > 0:
            return False
        return True

if __name__ == '__main__':
    S = Solution()
    s = "()"
    print(S.isValid(s))
    s = "()[]{}"
    print(S.isValid(s))
    s = "(]"
    print(S.isValid(s))
    s = "([])"
    print(S.isValid(s))