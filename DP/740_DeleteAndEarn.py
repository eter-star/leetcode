from collections import defaultdict
from functools import cache
from typing import List


# https://leetcode.com/study-plan/dynamic-programming/?progress=xrs8w3a5

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        max_points = [0] * (max_number + 1)
        max_points[1] = points[1]

        for num in range(2, len(max_points)):
            max_points[num] = max(max_points[num-1], max_points[num-2] + points[num])

        return max_points[max_number]


if __name__ == '__main__':
    # cost = [10, 15, 20]
    nums = [2, 2, 3, 3, 3, 4]
    res = Solution().deleteAndEarn(nums=nums)
    print(res)
