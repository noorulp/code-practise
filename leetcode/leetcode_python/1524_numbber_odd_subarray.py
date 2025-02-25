
class Solution:
    def numOfSubbArrays(self, arr: list[int]) -> int:
        res = 0
        evenArr = 0
        oddArr = 0
        sum = 0
        for num in arr:
            sum += num
            if sum % 2 == 0:
                evenArr += 1
            else:
                oddArr += 1
        sum = 0
        res += oddArr
        for num in arr:
            if num % 2 == 1: 
                oddArr -= 1
                # subtracting odd from odd number changes num to even and vice versa so swap
                oddArr, evenArr = evenArr, oddArr
            else:
                evenArr -= 1
            res += oddArr

        return res % (10**9 + 7)

def test(arr: list):
    sol = Solution()
    print(sol.numOfSubbArrays(arr))

if __name__ == '__main__':
    test(arr = [1,2,3,4,5,6,7])