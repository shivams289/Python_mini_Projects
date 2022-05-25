from queue import Queue


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left_node = None
        self.right_node = None

    def add_left_child(self, child):
        if not self.left_node:
            self.left_node = BinaryTree(child)

        else:
            self.left_node.add_left_child(child)

    def add_right_child(self, child):
        if not self.right_node:
            self.right_node = BinaryTree(child)

        else:
            self.right_node.add_right_child(child)

    ## Depth First Search(DFS)
    def pre_order(self):
        print(self.val, end=" ")
        if self.left_node:
            self.left_node.pre_order()

        if self.right_node:
            self.right_node.pre_order()

    def inorder(self):
        if self.left_node:
            self.left_node.inorder()

        print(self.val, end=" ")

        if self.right_node:
            self.right_node.inorder()

    def inorder2(self):
        if self.val is None:
            return

        self.left_node.inorder()

        print(self.val, end=" ")
        self.right_node.inorder()

    def post_order(self):
        if self.left_node:
            self.left_node.post_order()

        if self.right_node:
            self.right_node.post_order()

        print(self.val, end=" ")

    # Breadth First Search

    def bfs(self):
        q = Queue()
        q.put(self)
        while not q.empty():
            cur_node = q.get()
            print(cur_node.val, end=" ")
            if cur_node.left_node:
                q.put(cur_node.left_node)
            if cur_node.right_node:
                q.put(cur_node.right_node)


a_node = BinaryTree("a")
a_node.add_left_child("b")
a_node.add_right_child("c")

b_node = a_node.left_node
b_node.add_right_child("d")

c_node = a_node.right_node
c_node.add_left_child("e")
c_node.add_right_child("f")


a_node.pre_order()
print("PREORDER")

a_node.inorder()
print("INORDER")

a_node.post_order()
print("POSTORDER")


a_node.bfs()
print("BFS")

a_node.inorder2()
print("INORDER2")
