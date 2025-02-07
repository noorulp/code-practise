class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap = dict()
        n1 = len(s1)
        for char in s1:
            hashMap[char] = 1 + hashMap.get(char, 0)
        l = 0
        for i, char in enumerate(s2):
            cnt = hashMap.get(char, -1)
            if cnt == -1:
                # char does not exist
                while l < i:
                    hashMap[s2[l]] = hashMap[s2[l]] + 1
                    l += 1
                l = i + 1

            elif cnt > 0:
                hashMap[char] = hashMap[char] - 1
                if i - l + 1 == n1:
                    return True
            else:
                while l < i:
                    if s2[l] == char:
                        l += 1
                        break
                    hashMap[s2[l]] = hashMap[s2[l]] + 1
                    l += 1
                
        return False
    

if __name__ == '__main__':
    sol = Solution()
    s1 = "adc"
    s2 = "dcda"
    print(sol.checkInclusion(s1, s2))
    s1 = "ab"
    s2 = "eidbcabooo"
    print(sol.checkInclusion(s1, s2))
    