#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        best = sum(nums[:3])
        if target <= best:
            return best

        mag = sum(nums[-3:])
        if target >= mag:
            return mag

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = val + nums[left] + nums[right]
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    return threeSum

                if abs(best-target) > abs(threeSum-target):
                    best = threeSum

        return best
# @lc code=end
