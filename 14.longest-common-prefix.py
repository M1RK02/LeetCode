#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for element in strs[1:]:
            while not element.startswith(prefix):
                prefix = prefix[:-1]
                if len(prefix) == 0:
                    return ""

        return prefix
# @lc code=end
