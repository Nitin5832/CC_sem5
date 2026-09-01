class Solution(object):
    def rotate(self, matrix):
        n=len(matrix)
        result = [[0] * n for _ in range(n)]
        b=0
        for i in range(n):
            a=n-1
            for j in range(n):
                result[i][j]=matrix[a][b]
                a-=1
            b+=1
        matrix[:]=result
       



        
        