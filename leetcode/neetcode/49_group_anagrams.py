from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Less optimal
        """
        output_chars = defaultdict(list)
        for str in strs:
            # create char array
            str_arr = [0] * 26
            for i in str:
                str_arr[ord(i) - 97] += 1
            # check char array against output
            output_chars[tuple(str_arr)].append(str)
            
        return list(output_chars.values())


if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    str1 = [""]
    str2 = ["a"]
    str3 = ["a",""]
    S = Solution()
    print(S.groupAnagrams(strs))
    print(S.groupAnagrams(str1))
    print(S.groupAnagrams(str2))
    print(S.groupAnagrams(str3))