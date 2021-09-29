class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            while True:
                nums.pop(nums.index(val))
        except ValueError:
            return len(nums)
