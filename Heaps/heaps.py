class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2

        if left >= len(self.heap) and right >= len(self.heap):
            return
        
        if right < len(self.heap):
            self.heapify(right)
        if left < len(self.heap):
            self.heapify(left)

        while True:
            largest = i
            if left < len(self.head) and self.head[left] > self.head[i]:
                largest = left
            if right < len(self.head) and self.head[right] > self.head[i]:
                largest = right

            if largest != i:
                holder = self.heap[i]
                self.heap[i] = self.heap[largest]
                self.heap[largest] = holder
                i = largest
                left = 2 * i + 1
                right = 2 * i + 2
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self.heapify(0)

    def delete(self):
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.heapify(0)

class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2

        if left >= len(self.heap) and right >= len(self.heap):
            return
        
        if right < len(self.heap):
            self.heapify(right)
        if left < len(self.heap):
            self.heapify(left)

        while True:
            smallest = i
            if left < len(self.head) and self.head[left] < self.head[i]:
                smallest = left
            if right < len(self.head) and self.head[right] < self.head[i]:
                smallest = right

            if smallest != i:
                holder = self.heap[i]
                self.heap[i] = self.heap[smallest]
                self.heap[smallest] = holder
                i = smallest
                left = 2 * i + 1
                right = 2 * i + 2
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self.heapify(0)

    def delete(self):
        self.heap[0] = self.heap[-1]
        self.heap = self.heap[:-1]
        self.heapify(0)
