class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i + 1] == nums[i + 2]:
                del nums[i]
            else:
                i += 1