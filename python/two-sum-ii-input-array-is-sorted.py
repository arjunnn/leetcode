class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            if (target - num) in nums:
                solution = set([index + 1, nums.index(target - num) + 1])
                if len(solution) == 1:
                    continue
                return sorted(solution)
