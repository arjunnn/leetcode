from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) == 0:
            if k % 2 == 0:
                pass
            else:
                nums = reversed(nums)
        else:
            while k:
                num = nums.pop()
                nums.insert(0, num)
                k -= 1
