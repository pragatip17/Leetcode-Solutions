class Solution(object):
    def romanToInt(self, s):
        numerals={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        a=list(s)
        total=0
        for i in range (len(a)):
            m=numerals[a[i]]
            if i < len(a) - 1 and numerals[a[i]] < numerals[a[i + 1]]:
                m = -m
            
            total += m
        return total
                
                    
