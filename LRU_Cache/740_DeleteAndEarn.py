from collections import defaultdict
from functools import cache
from typing import List


# https://leetcode.com/study-plan/dynamic-programming/?progress=xrs8w3a5

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        @cache
        def max_points(num):
            # Check for base cases
            if num == 0:
                return 0
            if num == 1:
                return points[1]

            # Apply recurrence relation
            return max(max_points(num - 1), max_points(num - 2) + points[num])

        return max_points(max_number)


if __name__ == '__main__':
    # cost = [10, 15, 20]
    nums = [2, 2, 3, 3, 3, 4]
    res = Solution().deleteAndEarn(nums=nums)
    print(res)
