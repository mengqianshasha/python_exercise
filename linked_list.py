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
        iterate = self.head
        while iterate.next:
            iterate = iterate.next
        iterate.next = new_node
        self.size += 1

    def pop(self):
        if self.head.next is None:
            raise LinkedListEmptyError("Pop from empty linked list")
        else:
            iterate = self.head
            while iterate.next.next:
                iterate = iterate.next
            value = iterate.next.value
            iterate.next = None
            self.size -= 1
            return value

    def get_index(self, index):
        if self.head.next:
            iterate = self.head.next
            for i in range(index):
                iterate = iterate.next
            return iterate.value

    def delete(self, index):
        if self.head.next:
            iterate = self.head
            for i in range(index):
                iterate = iterate.next
            iterate.next = iterate.next.next
            self.size -= 1

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





