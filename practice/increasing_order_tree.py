# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        lst = []

        def inorder(root):
            if root.left:
                inorder(root.left)
            lst.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)
        print(lst)

        def addchild(r, child):
            if r.right:
                addchild(r.right, child)
            else:
                r.right = TreeNode(child)

            return r

        t = TreeNode(lst[0])
        for v in lst[1:]:
            addchild(t, v)

        return t
