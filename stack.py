class Stack:
    def __init__(self):
        self.content = []

    def push(self,add_item):
        self.content.append(add_item)

    def pop(self):
        if self.size() == 0:
            raise StackEmptyError("pop from empty stack")
        return self.content.pop()

    def top(self):
        return self.content[-1]

    def size(self):
        return len(self.content)

    def __str__(self):
        return 'Stack' + str(self.content)


class StackEmptyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


if __name__=="__main__":
    stack = Stack()
    stack.pop()



