# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def f(isi,iei,psi,pei):
            if isi>iei or psi>pei:
                return None
            root=TreeNode(postorder[pei])
            i=isi
            while inorder[i]!=root.val:
                i+=1
            lstnodes=i-isi
            root.left=f(isi,i-1,psi,psi+lstnodes-1)
            root.right=f(i+1,iei,psi+lstnodes,pei-1)
            return root        
        return f(0,len(inorder)-1,0,len(postorder)-1)