from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost) + 1)]
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[len(cost)]


if __name__ == '__main__':
    # cost = [10, 15, 20]
    cost = [1,100,1,1,1,100,1,1,100,1]
    res = Solution().minCostClimbingStairs(cost=cost)
    print(res)
