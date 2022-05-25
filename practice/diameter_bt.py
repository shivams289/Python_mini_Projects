# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        d1 = self.diameterOfBinaryTree(root.left)
        d2 = self.diameterOfBinaryTree(root.right)
        d3 = self.height(root.left) + self.height(root.right)
        print(d1, d2, d3)
        return max(max(d1, d2), d3)


# -----------------O(N) solution------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.dfs(root)

        return self.diameter

    def dfs(self, root):
        if not root:
            return 0

        leftCount = self.dfs(root.left)
        rightCount = self.dfs(root.right)

        self.diameter = max(self.diameter, leftCount + rightCount)

        return max(leftCount, rightCount) + 1
