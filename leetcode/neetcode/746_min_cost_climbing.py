
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        cost_0 = 0 # cost to reach zeroth element
        cost_1 = 0 # cost to reach 1st element - can jump over
        i_0 = 0
        i_1 = 1
        i_2 = 2
        cost_2 = 0
        while i_2 <= n:
            cost_2 = min(cost_0 + cost[i_0], cost_1 + cost[i_1])
            print(f'cost[{i_2}]:{cost_2} cost[{i_1}]:{cost_1} + {cost[i_1]} , cost[{i_0}]:{cost_0} + {cost[i_0]}')
            cost_0 = cost_1
            i_0 = i_1
            cost_1 = cost_2
            i_1 = i_2
            i_2 += 1
        
        return cost_2


def test(cost: list):
    sol = Solution()
    print(sol.minCostClimbingStairs(cost))

if __name__ == '__main__':
    test(cost = [10,15,20])
    test(cost = [1,100,1,1,1,100,1,1,100,1])