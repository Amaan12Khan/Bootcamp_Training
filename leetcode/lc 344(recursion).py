class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''left,right=0,len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1'''
        def reverse(l,r):
            if l>=r:
                return 
            s[l],s[r]=s[r],s[l]
            reverse(l+1,r-1)
        reverse(l=0,r=len(s)-1)