class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev=0
        temp=x
        while temp>0:
            re=temp%10
            rev=rev*10+re
            temp=temp//10
        if x==rev:
            return True
        else:
            return False
        