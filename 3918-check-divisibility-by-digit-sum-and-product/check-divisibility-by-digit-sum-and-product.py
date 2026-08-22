class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=str(n)
        sum,p=0,1
        for i in range(0,len(s)):
            k=int(s[i])
            sum+=k
            p*=k
        result=sum+p
        if n%result==0:
            return True
        else:
            return False