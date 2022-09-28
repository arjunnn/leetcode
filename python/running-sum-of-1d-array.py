class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = []
        for num in nums:
            len_sums = len(sums)
            if len_sums > 0:
                sums.append(sums[len_sums - 1] + num)
            else:
                sums.append(nums[0])
        return sums