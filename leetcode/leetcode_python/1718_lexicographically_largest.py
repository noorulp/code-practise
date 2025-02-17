
class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        res = [0] * (2 * n - 1)
        def sequence(seq: list[int], nums: set):
                if len(nums) == n - 1:
                    return True

                i = 0
                l = len(seq)
                valid = False
                while seq[i]:
                    i += 1
                nextNum = n
                while nextNum > 1:
                    if nextNum not in nums and seq[i] == 0 and seq[i + nextNum] == 0:
                        seq[i] = nextNum
                        seq[i + nextNum] = nextNum
                        nums.add(nextNum)
                        isValid = sequence(seq, nums)
                        if not isValid:
                            seq[i] = 0
                            seq[i + nextNum] = 0
                            nums.remove(nextNum)
                        else:
                            return True
                    nextNum -= 1

                return valid
        
        res[0] = n
        res[0 + n] = n
        nums = set()
        nums.add(n)
        sequence(res, nums)
        print(res)


def test(n: int):
    sol = Solution()
    print(sol.constructDistancedSequence(n))

if __name__ == '__main__':
    test(5)
    