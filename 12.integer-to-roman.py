#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        memo = {1:['I','V'], 2:['X','L'], 3:['C','D'], 4:['M']}
        numero = [int(i) for i in str(num)]
        unita = len(str(num))
        result = ''
        for cifra in numero:
            if cifra < 4:
                result += cifra*memo[unita][0]
            elif cifra == 4:
                result += memo[unita][0] + memo[unita][1]
            elif cifra == 9:
                result += memo[unita][0] + memo[unita+1][0]
            else:
                result += memo[unita][1] + memo[unita][0]*(cifra-5)
            unita -= 1
        return result
# @lc code=end