class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        c1,stack1=0,[]
        for c in word:
            if c!=ch or c1!=0:
                stack1.append(c)
            else:
                if c1==0:
                    stack1.append(ch)
                    stack1.reverse()
                    c1+=1
        return "".join(stack1)
        