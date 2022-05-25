# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0

        left = dfs(root.left)
        right = dfs(root.right)

        return root.val == root.left.val + root.right.val
