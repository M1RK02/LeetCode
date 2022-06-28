#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrice = [[] for _ in range(numRows)]
        char = 0

        while char < len(s):
            riga = 0
            while char < len(s) and riga < numRows:
                matrice[riga].append(s[char])
                riga += 1
                char += 1
            diagonale = numRows - 2
            while char < len(s) and diagonale > 0:
                matrice[diagonale].append(s[char])
                char += 1
                diagonale -= 1

        result = ""
        for line in matrice:
            print(line)
            for char in line:
                result += char
        return result
# @lc code=end
