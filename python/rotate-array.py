from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k % l == 0:
            if k % 2 != 0:
                nums = reversed(nums)
        else:
            if k > l:
                k = k % l
            while k != 0:
                val = nums.pop()
                nums.insert(0, val)
                k -= 1
