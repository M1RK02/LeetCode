#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": [
            "m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        result = []

        if len(digits) == 0:
            return result

        if len(digits) > 1:
            rec = self.letterCombinations(digits[1:])
        else:
            rec = [""]

        for element in rec:
            for letter in dict[digits[0]]:
                result.append(letter+element)

        return result
# @lc code=end
