from typing import List


# Top-Down Method

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        memo = {}

        def dp(op, left):
            if op == m:
                return 0
            if (op, left) in memo:
                return memo[(op, left)]

            l = nums[left] * multipliers[op] + dp(op + 1, left + 1)
            right = (n - 1) - (op - left)
            r = nums[right] * multipliers[op] + dp(op + 1, left)

            memo[(op, left)] = max(l, r)

            return memo[(op, left)]

        return dp(0, 0)


if __name__ == '__main__':
    nums = [-5, -3, -3, -2, 7, 1]
    multipliers = [-10, -5, 3, 4, 6]
    res = Solution().maximumScore(nums=nums, multipliers=multipliers)
    print(res)
