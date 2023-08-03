class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        a = []
        for sentence in sentences:
            a.append(len(sentence.split()))
        return max(a)




