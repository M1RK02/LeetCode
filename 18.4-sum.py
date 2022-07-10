#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums.sort()

        for i, val1 in enumerate(nums):
            if i > 0 and val1 == nums[i - 1]:
                continue

            j = i+1
            while j < len(nums):

                left, right = j+1, len(nums) - 1
                while left < right:
                    fourSum = val1 + nums[j] + nums[left] + nums[right]
                    if fourSum > target:
                        right -= 1
                    elif fourSum < target:
                        left += 1
                    else:
                        result.add((val1, nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1

                j += 1

        return result
# @lc code=end
