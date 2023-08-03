class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        for i in nums:
            a += i
        for i in nums:
            for j in str(i):
                b += int(j)
        return abs(a - b)