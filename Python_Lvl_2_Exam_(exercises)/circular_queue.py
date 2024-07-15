# Implement a Circular Queue
# Objective: Design a class `CircularQueue` that implements a circular queue with fixed size using a list.
# Parameters:
# - size: An integer representing the maximum number of elements the queue can hold.
# Returns:
# - None; methods handle the queue operations.
# Details:
# - Methods include `enqueue`, `dequeue`, `peek`, and `is_empty`.
# - `enqueue` should add an element to the queue if not full; otherwise, raise an exception.
# - `dequeue` should remove and return the element from the front if not empty; otherwise, raise an exception.
# - `peek` returns the front element without removing it.
# - `is_empty` checks whether the queue is empty.
# - Handle overflow and underflow appropriately with exceptions.

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    pass

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            raise Exception("Queue is full")
        elif self.is_empty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
        pass

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elif self.front == self.rear:
            data = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return data
        else:
            data = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return data
        pass

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]
        pass

    def is_empty(self):
        return self.front == -1
        pass


# Examples:
cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
print(cq.peek())  # Expected: 1
print(cq.dequeue())  # Expected: 1
print(cq.is_empty())  # Expected: False
cq.enqueue(3)
cq.enqueue(4)
print(cq.dequeue())  # Expected: 2
print(cq.dequeue())  # Expected: 3
