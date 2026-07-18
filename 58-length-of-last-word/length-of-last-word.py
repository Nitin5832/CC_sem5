class Solution(object):
    def lengthOfLastWord(self, s):
        k=0
        for i in range(-1,-(len(s)+1),-1):
            if s[i].isalpha():
                for j in range(i,-(len(s)+1),-1):
                    if s[j]==" ":
                        break
                    k+=1
                return k
                    
                    
                
                
        