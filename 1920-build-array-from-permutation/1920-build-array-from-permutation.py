class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[None]*n
        for i in range(len(nums)):
            ans[i]=nums[nums[i]]
        return ans
