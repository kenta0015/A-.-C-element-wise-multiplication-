class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def __len__(self):
        return self.size