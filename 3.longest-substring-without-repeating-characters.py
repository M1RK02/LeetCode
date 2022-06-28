#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 1
        start = 0
        end = 1
        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
            else:
                start += 1
            max_len = max(max_len, end - start)
        return max_len
# @lc code=end
