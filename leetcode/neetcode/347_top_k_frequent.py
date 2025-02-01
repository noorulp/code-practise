from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key in counts.keys():
            bucket[counts[key]].append(key)
        output = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                output.append(num)
                if len(output) == k:
                    return output



if __name__ == '__main__':
    S = Solution()
    nums = [1,1,1,2,2,2,3,3,3,3,3]
    k = 2
    out = S.topKFrequent(nums, k)
    print(out)