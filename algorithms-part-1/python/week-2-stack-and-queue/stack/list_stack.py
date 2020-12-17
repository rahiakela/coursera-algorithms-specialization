# Implementation of the Stack ADT using a Python list.

class Stack:

    def __init__(self):
        # Creates an empty stack.
        self._items = list()

    def is_empty(self):
        # Returns True if the stack is empty or False otherwise.
        return len(self) == 0

    def __len__(self):
        # Returns the number of items in the stack.
        return len(self._items)

    def peek(self):
        # Returns the top item on the stack without removing it.
        assert not self.is_empty(), "Cannot peek at an empty stack"
        return self._items[-1]

    def pop(self):
        # Removes and returns the top item on the stack.
        assert not self.is_empty(), "Cannot pop from an empty stack"
        return self._items.pop()

    def push(self, item):
        # Push an item onto the top of the stack.
        self._items.append(item)
