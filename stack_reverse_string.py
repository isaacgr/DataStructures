"""
Stack data structure.

D
C
B
A

"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

def reverse_string(stack, input_string):
    for char in range(len(input_string)):
        stack.push(input_string[char])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    print rev_str

stack = Stack()
reverse_string(stack, "hello")
