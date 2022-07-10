#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def ricorsione(result, temp, left, right) -> List[str]:
            if left == 0 and right == 0:
                result.append(temp)
            if left > 0:
                ricorsione(result, temp + "(", left-1, right)
            if right > left:
                ricorsione(result, temp + ")", left, right-1)

        ricorsione(result, "", n, n)
        return result
# @lc code=end
