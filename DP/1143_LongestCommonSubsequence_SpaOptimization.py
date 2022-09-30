# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1




if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    res = Solution().longestCommonSubsequence(text1, text2)
    print(res)
