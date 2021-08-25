class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num_index, num in enumerate(nums):
            if (target - num) in nums:
                solution =  set([num_index, nums.index(target-num)])
                if len(solution) == 1:
                    continue
                return solution
