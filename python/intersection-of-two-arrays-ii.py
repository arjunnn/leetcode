class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #         i = 0
        #         if len(nums2) > len(nums1):
        #             while i <= len(nums1) - 1:
        #                 if not nums1[i] in nums2:
        #                     nums1[i] = None
        #                 else:
        #                     nums2.pop(nums2.index(nums1[i]))
        #                 i += 1
        #             return [num for num in nums1 if num is not None]
        #         else:
        #             while i <= len(nums2) - 1:
        #                 if not nums2[i] in nums1:
        #                     nums2[i] = None
        #                 else:
        #                     nums1.pop(nums1.index(nums2[i]))
        #                 i += 1
        #             return [num for num in nums2 if num is not None]

        from collections import Counter

        return (Counter(nums1) & Counter(nums2)).elements()
