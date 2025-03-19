
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        steps = 0
        n = len(nums) - 2
        i = 0
        while i < n:
            if nums[i] == 0:
                # flip
                steps += 1
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
            i += 1
        
        if nums[i] == 1 and nums[i + 1] == 1:
            return steps
        return -1

def test(nums: list, output: int):
    sol = Solution()
    res = sol.minOperations(nums)
    print(res)
    assert res == output

if __name__ == '__main__':
    test([0,1,1,1,0,0], 3)
    test([0,1,1,1], -1)