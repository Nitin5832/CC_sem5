class Solution(object):
    def findRelativeRanks(self, score):
        matrix=[]
        m=4
        res = [""] * len(score)
        for i in range(len(score)):
            matrix.append([score[i],i])
        
        matrix.sort(reverse=True)
        print(matrix)

        for r in range(len(score)):
            k = matrix[r][1]

            if r == 0:
                res[k] = "Gold Medal"
            elif r == 1:
                res[k] = "Silver Medal"
            elif r == 2:
                res[k] = "Bronze Medal"
            else:
                res[k] = str(r + 1)

        return res




        

        
        