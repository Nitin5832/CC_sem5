class Solution(object):
    def countCommas(self, n):
        res=0
        m=1000
        while (m<=n):
            res+=n-m+1
            m*=1000
        return res
        