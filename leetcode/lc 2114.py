class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        ans=0
        for i in sentences:
            ans=len(i.split())
            if ans>maxi:
                maxi=ans
        return maxi