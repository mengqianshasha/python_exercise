class MyQueue:
    def __init__(self):
        self.content = []

    def enqueue(self,add_item):
        self.content.append(add_item)

    def dequeue(self):
        if self.size() == 0:
            raise QueueEmptyError("dequeue from empty queue")
        return self.content.pop(0)

    def peak(self):
        return self.content[0]

    def size(self):
        return len(self.content)

    def __str__(self):
        return 'Queue' + str(self.content)


class QueueEmptyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


if __name__=="__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)

    print(queue.dequeue())
    print(queue.peak())
    print(queue.size())




