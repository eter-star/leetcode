from typing import List

# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/


# Bottom_Up Method

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):
                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])

        return dp[0][0]


if __name__ == '__main__':
    nums = [-5, -3, -3, -2, 7, 1]
    multipliers = [-10, -5, 3, 4, 6]
    res = Solution().maximumScore(nums=nums, multipliers=multipliers)
    print(res)
