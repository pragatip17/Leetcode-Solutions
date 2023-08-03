class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        a=[None]*2*n
        for i in range(n):
            a[2*i] = nums[i]
            a[2*i+1] = nums[n+i]
        return a

