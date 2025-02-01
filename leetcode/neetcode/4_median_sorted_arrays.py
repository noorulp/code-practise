class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        nA = len(A)
        nB = len(B)
        n = nA + nB
        half = (len(A) + len(B)) // 2
        leftA = 0
        rightA = len(A) - 1
        while True:
            midA = (leftA + rightA)// 2
            # B partition
            midB = half - midA - 2
            lA = A[midA] if midA >= 0 else float('-inf')
            rA = A[midA + 1] if midA + 1 < nA else float('inf')
            lB = B[midB] if midB >=0 else float('-inf')
            rB = B[midB + 1] if midB + 1 < nB else float('inf')
            # left partition A should be less than all of right partition B
            # left partition B should be less than all of right partition A
            if lA <= rB and lB <= rA:
                # correct partition
                if n % 2 == 0:
                    return (max(lA, lB) + min(rA, rB)) / 2
                else:
                    return min(rA, rB)
            elif rA < lB:
                # increase left partition
                leftA = midA + 1
            else:
                # decrease left partition
                rightA = midA - 1


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,2,3,4,5,6,7,8,9]
    nums2 = [1,2,3,4]
    print(sol.findMedianSortedArrays(nums1, nums2))
    nums1 = [1,3]
    nums2 = [2]
    print(sol.findMedianSortedArrays(nums1, nums2))
    nums1 = [1,2]
    nums2 = [3,4]
    print(sol.findMedianSortedArrays(nums1, nums2))