class Solution(object):
    def convertToTitle(self, columnNumber):
        s=""
        a=columnNumber

        if a<=26:
            return chr(a+64)

        while a>0:
            if a%26 == 0:
                b=90
            else :
                b=a%26+64
            s+=chr(b)    
            a=a//26

            if s[-1]=='Z':
                a-=1

        return s[::-1]




    
            

        