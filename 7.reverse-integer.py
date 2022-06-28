#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:

        new_x = int(str(abs(x))[::-1])

        if new_x > 2**31:
            return 0

        if x > 0:
            return new_x
        else:
            return -new_x
# @lc code=end
