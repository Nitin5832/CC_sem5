class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!= len(t):
            return False
        d1={}
        assigned=set()
        for i in range (len(s)):
            if s[i] in d1:
                if d1[s[i]] != t[i]:
                    return False
            else :
                if t[i] in assigned:
                    return False
                d1[s[i]]=t[i]
                assigned.add(t[i])
        return True

            

            
        
        