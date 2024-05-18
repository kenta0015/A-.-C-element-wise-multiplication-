class CircularArrayQueue:
    def __init__(self, capacity=10):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = -1

def IsEmpty(self):
        return self.size == 0
    
def __len__(self):
        return self.size

def __str__(self):
        if self.IsEmpty():
            return "Queue is empty"
        return str([self.queue[(self.front + i) % self.capacity] for i in range(self.size)])