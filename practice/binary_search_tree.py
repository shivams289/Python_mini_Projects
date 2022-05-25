from multiprocessing.sharedctypes import Value
from xml.dom.expatbuilder import parseFragment


class BST:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_child(self, child):
        if (
            self.left_child and child <= self.value
        ):  # if there's left child and child is less than that
            self.left_child.insert_child(child)

        elif (
            child <= self.value
        ):  # if No left child, means leaf node create a BST again
            self.left_child = BST(child)

        elif self.right_child and child >= self.value:
            self.right_child.insert_child(child)

        else:
            self.right_child = BST(child)

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.value, end=" ")

        if self.right_child:
            self.right_child.inorder()

    def height(self, root):
        if self.root is None:
            return 0
        else:
            return 1 + max(self.right_child.height(), self.left_child.height())

    def search_value(self, key):
        if self.value == key:
            return True

        if key > self.value and self.right_child:
            return self.right_child.search_value(key)

        if key < self.value and self.left_child:
            return self.left_child.search_value(key)

        else:
            return False

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def find_min_value(self):
        if self.left_child:
            return self.left_child.find_min_value()

        else:
            return self.value

    def remove_node(self, value, parent):
        if self.left_child and value < self.value:
            return self.left_child.remove_node(value, parent)
        elif (
            value < self.value
        ):  # at the end of left leaf..no more values to explore. not dound
            return False

        elif self.right_child and value > self.value:
            return self.right_child.remove_node(value, parent)

        elif value > self.value:
            return False
        else:
            if (
                self.left_child is None
                and self.right_child is None
                and self == parent.left_child
            ):  # self is a leaf node, left node of a given parent
                parent.left_child = None
                self.clear_node()
            elif (
                self.left_child is None
                and self.right_child is None
                and self == parent.right_child
            ):  # self is a leaf node, right node of a given parent
                parent.right_child = None
                self.clear_node()

            elif (
                self.left_child
                and self.right_child is None
                and self == parent.left_child
            ):  # self has a left child and is a left child of parent node
                parent.left_child = self.left_child
                self.clear_node()

            elif (
                self.left_child
                and self.right_child is None
                and self == parent.right_child
            ):  # self has a left child and is a right child of parent node
                parent.right_child = self.left_child
                self.clear_node()

            elif (
                self.right_child
                and self.left_child is None
                and self == parent.left_child
            ):  # self has a right child and is a left child of parent node
                parent.left_child = self.right_child
                self.clear_node()

            elif (
                self.right_child
                and self.left_child is None
                and self == parent.right_child
            ):  # self has a right child and is a right child of parent node
                parent.right_child = self.right_child
                self.clear_node()

            else:  # node having both left and right kids
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(
                    self.value, self
                )  # right child ka adress dediya, remove krna wala node,

            return True  # Node deleted

    def count_of_nodes(self):
        if not self.val:
            return 0

        return self.right_node.count_of_nodes() + self.left_node.count_of_nodes() + 1

    def sum_of_nodes(self):
        right, left = 0, 0
        if self.right_node:
            right = self.right_node.sum_of_nodes()

        elif self.left_node:
            left = self.left_node.sum_of_nodes()

        return right + left + self.val

    def height(self):
        if not self.val:
            return 0
        right, left = 0, 0
        if self.right_node:
            right = self.right_node.height()

        elif self.left_node:
            left = self.right_node.height()

        return max(left, right) + 1


tree_node = BST(10)

lst = [5, 2, 9, 7, 1, 15]
for e in lst:
    tree_node.insert_child(e)
print(tree_node.height(), "height")
tree_node.inorder()
print("INORDER")

print(tree_node.search_value(6), "FIND VALUE")
# print("height", a_node.height())
print("countofnode", tree_node.sum_of_nodes())

# print("countofnode", a_node.count_of_nodes())
