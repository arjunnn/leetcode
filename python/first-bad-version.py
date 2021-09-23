# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while True:
            if start == end:
                return start
            mid_point = start + int((end - start)/2)
            if isBadVersion(mid_point):
                end = mid_point
            elif start + 1 == end:
                return end
            else:
                start = mid_point
        return mid_point
        