class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int: 
        hashMap = {}
        for num in arr:
            hashMap[num] = set()
        maxLen = 0
        n = len(arr)
        for i in range(1, n - 2):
            
            for j in range(0, i):
                prev = arr[j]
                cur = arr[i]
                count = 2
                while hashMap.get(prev + cur, None) is not None:
                    num = prev + cur
                    if cur in hashMap.get(num):
                        break
                    hashMap.get(num).add(cur)
                    prev = cur
                    cur = num
                    count += 1
                if count > 2:
                    maxLen = max(maxLen, count)

        return maxLen

def test(arr: list):
    sol = Solution()
    print(sol.lenLongestFibSubseq(arr))

if __name__ == '__main__':
    test(arr = [1,2,3,4,5,6,7,9,11,18,29])