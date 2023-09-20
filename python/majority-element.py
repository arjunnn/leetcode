from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = nums[0]
        count = 1
        for num in nums:
            if num != val:
                count -= 1
                if count == 0:
                    val = num
                    count = 1
            else:
                count += 1
        return val
