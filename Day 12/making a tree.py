class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root=TreeNode(5)

root.left=TreeNode(6)
root.right=TreeNode(7)

root.left.left=TreeNode(8)
root.left.right=TreeNode(9)

root.left.right.left=TreeNode(1)

print(root)


def preorder(root):
    if root is None:
        return
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

preorder(root)
