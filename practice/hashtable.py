class HashtableNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None  # separatechaining


class Hashtable:
    def __init__(self) -> None:
        initial_capacity = 15
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
        hashsum = hashsum % self.capacity  # to keep it in  range of self.capacity

    def insert(self, key, value):
        self.size += 1  # increase the size
        index = self.hash(key)  # calculate the hashindex
        node = self.buckets[index]  # get the value in the list at that index
        # Create node, add it, return
        if node is None:
            self.buckets[index] = HashtableNode(key, value)
            return
        # 4. Collision! Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = HashtableNode(
            key, value
        )  # Add a new node at the end of the list with provided key/value

    def find(self, key):
        index = self.hash(key)  # calculate the hash
        node = self.buckets[index]  # check if that hash value is None
        if node is None:
            return None

        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while (
            node is not None and node.value != key
        ):  # iterate the linked list for the key
            prev = node
            node = node.next

        if node is None:
            return None

        else:
            # key found
            self.size -= 1
            result = node.value
            if prev is None:
                node = None

            else:
                prev.next = prev.next.next

            return result
