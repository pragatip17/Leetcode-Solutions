class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1,n*2+1):
            if(i%2==0):
                if(i%n==0):
                    return i
                    break