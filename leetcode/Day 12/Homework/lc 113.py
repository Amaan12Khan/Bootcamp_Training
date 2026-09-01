# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def dfs(node, remaining_sum, current_path):
            if not node:
                return
            
            # Add current node to path
            current_path.append(node.val)
            
            # Check if it's a leaf and sums up correctly
            if not node.left and not node.right and remaining_sum == node.val:
                result.append(list(current_path))
            else:
                # Recurse left and right
                dfs(node.left, remaining_sum - node.val, current_path)
                dfs(node.right, remaining_sum - node.val, current_path)
                
            # Backtrack
            current_path.pop()
            
        dfs(root, targetSum, [])
        return result