class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # try:
        #     while True:
        #         nums.pop(nums.index(val))
        # except ValueError:
        #     return len(nums)
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start] = nums[end]
                nums[end] = nums[start]
                end -= 1
            else:
                start += 1
            print(nums)
        return start
