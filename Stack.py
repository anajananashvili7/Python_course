class Stack:
    def __init__(self):
        self.stack = []

   
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None  

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0
