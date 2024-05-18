class CircularArrayQueue:
    def __init__(self, capacity=10):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = -1
