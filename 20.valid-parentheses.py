#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 != 0):
            return False

        stack = []
        brackets = {"}": "{", ")": "(", "]": "["}

        for char in s:
            if len(stack) == 0 or char not in brackets:
                stack.append(char)
            else:
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
# @lc code=end
