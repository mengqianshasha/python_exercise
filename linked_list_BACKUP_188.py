class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedListEmptyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class WrongIndexError(Exception):
    def __init__(self, message):
        self.message.message
        super().__init__(self.message)

class LinkedListIterator:
    def __init__(self, linked_list):
        self.linked_list = linked_list
        self.iterate = linked_list.head

    def __next__(self):
        if self.iterate.next:
            value = self.iterate.next.value
            self.iterate = self.iterate.next
            return value
        else:
            raise StopIteration()


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def append(self, new_value):
        new_node = Node(new_value)
        last_node = self.__find_node__(self.size - 1)
        self.__insert__after__(last_node, new_node)

    def pop(self):
        if self.head.next is None:
            raise LinkedListEmptyError("Pop from empty linked list")
        else:
            node_prev = self.__find_node__(self.size - 2)
            value = node_prev.next.value
            self.__delete_node__(node_prev)
            return value

    def get_value(self, index):
        return self.__find_node__(index).value

    def delete(self, index):
        prev_node = self.__find_node__(index - 1)
        self.__delete_node__(prev_node)

    def insert(self, index, value):
        node = self.__find_node__(index)
        new_node = Node(value)
        self.__insert__after__(node, new_node)

    def __find_node__(self, index):
        if index == -1:
            return self.head
        else:
            iterate = self.head
            for _ in range(index + 1):
                iterate = iterate.next
            return iterate

<<<<<<< HEAD
    def is_empty(self):
        return self.size == 0

    def has_cycle(self):
        pass

    def detect_cycle(self):
        pass

    def merge_sorted_list(self, sort_list):
        pass

    def reverse(self):
        pass

    def reverse_between(self, start, end):
        pass
=======
    def __delete_node__(self, node_prev):
        node = node_prev.next
        node_prev.next = node.next
        node.next = None
        self.size -= 1

    def __insert__after__(self, node, new_node):
        new_node.next = node.next
        node.next = new_node
        self.size += 1

    def is_empty(self):
        return self.size == 0

    def has_cycle(self):
        iterate1 = self.head
        iterate2 = self.head
        while iterate1.next and iterate2.next.next:
            iterate1 = iterate1.next
            iterate2 = iterate2.next.next
            if iterate1 == iterate2:
                return True
        return False

    def detect_cycle(self):
        iterate1 = self.head
        iterate2 = iterate1

        while iterate1.next:
            iterate1 = iterate1.next
            iterate2 = iterate2.next.next
            if iterate1 == iterate2:
                iterate3 = self.head
                break
        else:
            return None

        while iterate1 != iterate3:
            iterate1 = iterate1.next
            iterate3 = iterate3.next
        else:
            return iterate1

    def merge_sorted_list(self, sort_list):
        iterate = self.head
        iterate1 = iterate.next
        iterate2 = sort_list.head.next

        while iterate1 and iterate2:
            if iterate2.value <= iterate1.value:
                iterate_temp = iterate2.next
                iterate.next = iterate2
                iterate2.next = iterate1
                iterate = iterate2
                iterate2 = iterate_temp
            else:
                iterate = iterate1
                iterate1 = iterate1.next
        else:
            if iterate2:
                iterate.next = iterate2
        self.size += sort_list.size

    def reverse(self):
        iterate1 = None
        iterate2 = self.head.next
        while iterate2:
            node = iterate2.next
            iterate2.next = iterate1
            iterate1 = iterate2
            iterate2 = node
        self.head.next = iterate1

    def reverse_between(self, start, end):
        if self.size - 1 >= end >= start >= 0:
            node_prev = self.__find_node__(start - 1)
            node_end = self.__find_node__(end)
            node_after = node_end.next

            iterate1 = node_prev.next
            iterate2 = iterate1.next

            node_prev.next = node_end
            iterate1.next = node_after

            while iterate2 != node_after:
                node_temp = iterate2.next
                iterate2.next = iterate1
                iterate1 = iterate2
                iterate2 = node_temp

        else:
            raise LinkedListEmptyError("reverse empty linked list")

    def __iter__(self):
        return LinkedListIterator(self)

    def __getitem__(self, key):
        return self.get_value(key)
>>>>>>> 773362e37d57819c55d912ba0f34c5b750caabe4

    def __iter__(self):
        return LinkedListIterator(self)

if __name__ == "__main__":

    link = LinkedList()
    link.append(1)
    link.append(2)
    link.append(3)

    for i in link:
        print(i)
    for i in link:
        print(i)





