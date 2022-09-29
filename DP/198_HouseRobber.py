from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxRobbedAmount = [0 for _ in range(len(nums) + 1)]
        N = len(nums)

        '''We set maxRobbedAmount[N] to 0 since this means the robber doesn't 
        have any houses left to rob, thus zero profit. 
        Additionally, we set maxRobbedAmount[N - 1] to nums[N - 1] 
        because in this case, there is only one house to rob which is the last house. 
        Robbing it will yield the maximum profit.'''
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

        for i in range(N - 2, -1, -1):
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])

        return maxRobbedAmount[0]


if __name__ == '__main__':
    # cost = [10, 15, 20]
    nums = [2, 7, 9, 3, 1]
    res = Solution().rob(nums=nums)
    print(res)
