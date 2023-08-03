class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = [int(x) for x in str(n)]
        c=1
        d=0
        for i in range(len(b)):
            c*=b[i]
            d+=b[i]
        return (c-d)
