class Solution:

    def encode(self, strs: list[str]) -> str:
        output = ""
        for string in strs:
            output = f'{output}{len(string)}#{string}'
        return output

    def decode(self, s: str) -> list[str]:
        output = []
        i = 0
        l = len(s)
        while i<l:
            num = 0
            while s[i]!='#':
                num = num*10 + (ord(s[i]) - ord('0'))
                i += 1
            i += 1 # skip '#'
            output.append(s[i:i+num])
            i += num # next str
        return output

if __name__ == '__main__':
    S = Solution()
    input = ["we1234567890","say",":","yes"]
    output = S.encode(input)
    assert input == S.decode(output)