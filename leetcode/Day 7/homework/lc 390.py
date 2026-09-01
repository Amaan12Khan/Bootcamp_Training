class Solution:
    def lastRemaining(self, n: int) -> int:
        left=True
        remain=n
        step=1
        head=1
        while remain>1:
            if left or remain %2==1:
                head+=step
            step*=2
            remain//=2
            left=not left
        return head