#validate binary search tree
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def Validate(root, max, min):
            if root is None:
                return True
            if root.val <= min or root.val >= max:
                return False
            leftValid = Validate(root.left, root.val, min)
            rightValid = Validate(root.right, max, root.val)
            return leftValid and rightValid
        return Validate(root, float("inf"), float("-inf"))