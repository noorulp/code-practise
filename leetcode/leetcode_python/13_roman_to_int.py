class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        valueMap = dict()
        valueMap['I'] = 1
        valueMap['V'] = 5
        valueMap['X'] = 10
        valueMap['L'] = 50
        valueMap['C'] = 100
        valueMap['D'] = 500
        valueMap['M'] = 1000
        ordMap = dict()
        ordMap['I'] = 1
        ordMap['V'] = 2
        ordMap['X'] = 3
        ordMap['L'] = 4
        ordMap['C'] = 5
        ordMap['D'] = 6
        ordMap['M'] = 7
        for i, char in enumerate(s):
            if i > 0:
                if ordMap[s[i-1]] < ordMap[s[i]]: # eg I precedes V i.e. 4
                    num = num - 2 * valueMap[s[i-1]] + valueMap[s[i]]
                else:
                    num += valueMap[char]
            else:
                num += valueMap[char]
        
        return num


if __name__ == '__main__':
    s = 'MCMXCIV'
    sol = Solution()
    print(sol.romanToInt(s))