class Node:
    def __init__(self, data=None, next=None) -> None:
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def insertbegin(self, data):
        self.head = Node(data, None)

    def insertend(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_list_values(self, lst):
        self.head = None
        for el in lst:
            self.insertend(el)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def removeat(self, index):
        if index == 0:
            self.head = self.head.next
            return

        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")

        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insertat(self, key, index):
        if index == 0:
            self.head = self.head.next
            return

        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
