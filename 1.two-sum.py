#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, x in enumerate(nums):
            try:
                y = nums.index(target-x, index+1)
            except:
                continue
            return [index, y]
# @lc code=end