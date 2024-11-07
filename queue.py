# Queue implementation in Python
class Queue():
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, val):
        if not self.IsFull():
            self.queue.append(val)
        else:
            print("Queue is full")

    def dequeue(self):
        holder = self.queue[0]
        del self.queue[0]
        return holder

    def peek(self):
        return self.queue[0]

    def rear(self):
        return self.queue[-1]

    def IsFull(self):
        return len(self.queue) == self.max_size

    def IsEmpty(self):
        return len(self.queue) == 0
