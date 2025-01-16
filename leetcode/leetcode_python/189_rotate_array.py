
def reverse( nums: list[int], i, j) -> None:
    """
    reverse nums from i to j
    """
    left: int = i
    right: int = j
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1

def rotate( nums: list[int], k: int) -> None:
    """
    rotate array by k
    """
    # reverse 0..n-k-1
    n = len(nums)
    k = k % n
    reverse(nums, 0, n-k-1)
    # reverse n-k, n-1
    reverse(nums, n-k, n-1)
    # reverse the resulted array
    reverse(nums, 0, n-1)

class Solution:
    def rotate2(self, nums: list[int], k: int) -> int:
        n = len(nums)
        k = k % n
        # reverse 1st n - k nums
        print(nums[(n-k-1)::-1])
        # reverse last k nums
        print(nums[:-k-1:-1])
        # reverse result array
        nums = (nums[(n-k-1)::-1] + nums[:-k-1:-1])[::-1]
        print(nums)

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 11
    sol = Solution()
    sol.rotate2(x, k)
    print(x)
    rotate(x, k)
    print(x)