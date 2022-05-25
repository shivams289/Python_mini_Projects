# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def isSym(Left, Right):
            if not Left and not Right:
                return True
            if Left and Right and Left.val == Right.val:
                return isSym(Left.left, Right.right) and isSym(Left.right, Right.left)
            return False

        return isSym(root.left, root.right)
