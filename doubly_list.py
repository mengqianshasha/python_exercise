class ListEmptyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class DoublyListIterator:
    def __init__(self, doubly_list):
        self.doubly_list = doubly_list
        self.iterate = doubly_list.head

    def __next__(self):
        if self.iterate.next != self.doubly_list.tail:
            value = self.iterate.next.value
            self.iterate = self.iterate.next
            return value
        else:
            raise StopIteration()


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, value):
        self.__add_between__(self.tail.prev, self.tail, value)

    def pop(self):
        if self.head.next == self.tail:
            raise ListEmptyError("pop from empty doubly linked list")
        else:
            value = self.tail.prev.value
            self.__delete_node__(self.tail.prev)
            return value

    def get_index(self, index):
        iterate = self.__search_node__(index)
        return iterate.value

    def insert(self, index, value):
        iterate = self.__search_node__(index)
        self.__add_between__(iterate, iterate.next, value)

    def delete(self, index):
        node = self.__search_node(index)
        self.__delete_node__(node)

    def isEmpty(self):
        return self.size == 0

    def __search_node__(self, index):
        iterate = None
        if index <= self.size - 1 - index:
            iterate = self.head
            for i in range(index + 1):
                iterate = iterate.next
        else:
            iterate = self.tail
            for i in range(self.size - index):
                iterate = iterate.prev
        return iterate

    def __add_between__(self, node_before, node_after, value):
        new_node = Node(value)
        new_node.prev = node_before
        new_node.next = node_after
        node_before.next = new_node
        node_after.prev = new_node
        self.size += 1

    def __delete_node__(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        self.size -= 1

    def __iter__(self):
        return DoublyListIterator(self)


