class Solution(object):
    def totalFruit(self, fruits):
        dict1={}
        size=0
        low=0
        for i in range (len(fruits)):
            if fruits[i] not in dict1:
                dict1[fruits[i]]=1
            else:
                dict1[fruits[i]]+=1

            while (len(dict1)>2):
                dict1[fruits[low]]-=1
                if dict1[fruits[low]]==0:
                    del dict1[fruits[low]]
                low+=1
                
            if size<i-low+1:
                size=i-low+1
        return size


        
        