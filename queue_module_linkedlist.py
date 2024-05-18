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
    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            raise KeyError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.rear = None
        return data
    
    def peek(self):
        if self.is_empty():
            raise KeyError("Queue is empty")
        return self.front.data
    
    def __contains__(self, data):
        current = self.front
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        current_self = self.front
        current_other = other.front
        while current_self:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True
    
    def clear(self):
        self.front = self.rear = None
        self.size = 0