class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count=0
        if ruleKey=="type":
            for i in range(len(items)):
                if items[i][0]==ruleValue:
                    count+=1
        elif ruleKey=="color":
            for i in range(len(items)):
                if items[i][1]==ruleValue:
                    count+=1
        elif ruleKey=="name":
            for i in range(len(items)):
                if items[i][2]==ruleValue:
                    count+=1
        return count