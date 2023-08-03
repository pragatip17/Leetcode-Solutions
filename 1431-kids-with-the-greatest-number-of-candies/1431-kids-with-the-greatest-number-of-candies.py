class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n=len(candies)
        a=[]
        for i in range(n):
            if candies[i]+extraCandies >= max(candies):
                a.append(True)
            else:
                a.append(False)
        return a
