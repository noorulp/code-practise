
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        # f(n) = f(n-1) + f(n-2)
        n_0 = 1
        n_1 = 2
        n_2 = 0
        i = 2
        while i < n:
            n_2 = n_1 + n_0
            n_0 = n_1
            n_1 = n_2
            i += 1

        return n_2 

def test(n: int):
    sol = Solution()
    print(sol.climbStairs(n))

if __name__ == "__main__":
    test(3)
    test(2)
    test(5)
