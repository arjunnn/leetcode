from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = list(sorted(nums1 + nums2))
        if len(merged_array) == 1:
            return merged_array[0]
        is_even = len(merged_array) % 2 == 0
        midpoint = len(merged_array) // 2
        if is_even:
            return (merged_array[midpoint - 1] + merged_array[midpoint]) / 2
        return merged_array[midpoint]
