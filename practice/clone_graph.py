"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if node is None:
            return None

        new = {}

        def clone(node):
            if node in new:
                return new[node]

            copy = Node(node.val)
            new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy

        return clone(node)
