class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        previous = None
        if not nums:
            return 0
        last_pos = 0
        for i in range(len(nums)):
            if nums[i] != nums[last_pos]:
                last_pos += 1
            nums[last_pos] = nums[i]
        return last_pos + 1
