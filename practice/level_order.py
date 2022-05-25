from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if root is None:
            return output

        q = Queue()
        q.put(root)
        while not q.empty():
            count = q.qsize()
            lst = []
            while count > 0:
                node = list(q.queue)[0]
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
                count -= 1
                lst.append(node.val)
                q.get()
            output.append(lst)

        return output
