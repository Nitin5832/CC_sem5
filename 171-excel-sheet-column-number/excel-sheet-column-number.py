class Solution(object):
    def titleToNumber(self, columnTitle):
        a=0
        for i in range(len(columnTitle)):
            a+=26**(i)*(ord(columnTitle[-i-1])-64)
        return a

        

        