class Solution(object):
    def longestCommonPrefix(self, strs):
    
        prefix=''
        if not strs:
            return prefix
        prefix=strs[0]

        for i in range (len(strs)):
            while strs[i].find(prefix) !=0:
                prefix=prefix[:-1]
                
        return prefix