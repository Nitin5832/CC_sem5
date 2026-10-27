class Solution(object):
    def createGrid(self, m, n):
        ans=[["#" for _ in range(n)] for _ in range(m)]
        
        k=0
        while(k<n):
            ans[0][k]='.'
            k+=1
        
        k=1
        while(k<m):
            ans[k][n-1]='.'
            k+=1
        
        return ["".join(row) for row in ans]



        