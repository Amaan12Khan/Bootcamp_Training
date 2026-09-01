# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(node, current_path):
            if not node:
                return
            
            # Append current node value to the path string
            if current_path:
                current_path += "->" + str(node.val)
            else:
                current_path = str(node.val)
                
            # If it's a leaf node, save the path
            if not node.left and not node.right:
                result.append(current_path)
            else:
                # Continue traversal on children
                dfs(node.left, current_path)
                dfs(node.right, current_path)
                
        dfs(root, "")
        return result
