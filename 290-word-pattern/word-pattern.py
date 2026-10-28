class Solution(object):
    def wordPattern(self, pattern, s):
        dict1={}
        list1=s.split()
        n=0

        if len(list1) != len(pattern):
            return False

        for word in pattern:
            if word not in dict1:
                if list1[n] in dict1.values():
                    return False
                dict1[word]=list1[n]
                
            else:             
                if dict1[word]!=list1[n]:
                    return False
            n+=1
        return True


        
        