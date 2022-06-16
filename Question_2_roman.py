class Solution:
    def romanToInt(self, s: str) -> int:
        l=['I','V','X','L','C','D','M']
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        S=0
        q=1
        for i in s[::-1]:
            if(d[i]<S):
                if(d[i]==q):
                    S+=d[i]
                    q=d[i]
                else:
                    S-=d[i]
            else:
                S+=d[i]
                q=d[i]
        return S