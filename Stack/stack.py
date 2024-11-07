#An implementation of the stack datastructure in Python
class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push_stack(self, val):
        if not self.isFull():
            self.stack.append(val)
        else:
            print("Stack Full")

    def pop_stack(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    @property
    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.max_size
