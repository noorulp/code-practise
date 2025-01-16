
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        l = m + n - 1

        while l >= 0:
            if i < 0:
                nums1[l] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[l] = nums1[i]
                i -= 1
            else:
                if nums1[i] > nums2[j]:
                    nums1[l] = nums1[i]
                    i -= 1
                else:
                    nums1[l] = nums2[j]
                    j -= 1

            l -= 1 


if __name__ == '__main__':
    
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    n = len(nums2)
    m = len(nums1) - n
    sol: Solution = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)