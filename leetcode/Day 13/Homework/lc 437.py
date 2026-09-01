# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, currSum):
            if not node:
                return 0

            currSum += node.val

            # Number of paths whose sum is targetSum
            count = prefix[currSum - targetSum]

            prefix[currSum] += 1

            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)

            # Backtrack
            prefix[currSum] -= 1

            return count

        return dfs(root, 0)