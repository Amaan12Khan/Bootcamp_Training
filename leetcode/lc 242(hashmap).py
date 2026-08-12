class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        k={}
        m={}
        for i in s:
            m[i]=m.get(i,0)+1
        for j in t:
            k[j]=k.get(j,0)+1
        return m==k