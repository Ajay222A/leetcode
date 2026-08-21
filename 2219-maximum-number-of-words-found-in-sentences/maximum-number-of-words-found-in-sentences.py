class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for i in range(len(sentences)):
            temp=0
            for j in sentences[i]:
                if j == ' ':
                    temp+=1
            ans=max(ans,temp)
        return ans+1
                