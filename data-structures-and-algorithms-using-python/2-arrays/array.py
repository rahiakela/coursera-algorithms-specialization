# Implements the Array ADT using array capabilities of the ctypes module.
import ctypes
import random


class Array:

    def __init__(self, size):
        """Creates an array with size elements."""
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        # Initialize each element.
        self.clear(None)

    def __len__(self):
        """Returns the size of the array."""
        return self._size

    def __getitem__(self, index):
        """Gets the contents of the index element."""
        assert 0 <= index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        """Puts the value in the array element at index position."""
        assert 0 <= index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        """Clears the array by setting each element to the given value."""
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """Returns the array's iterator for traversing the elements."""
        return _ArrayIterator(self._elements)


# An iterator for the Array ADT.
class _ArrayIterator:

    def __init__(self, arr):
        self._array_ref = arr
        self._curr_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curr_index < len(self._array_ref):
            entry = self._array_ref[self._curr_index]
            self._curr_index += 1
            return entry
        else:
            raise StopIteration


if __name__ == "__main__":

    # The constructor is called to create the array.
    value_list = Array(100)

    # Fill the array with random floating-point values.
    for i in range(len(value_list)):
        value_list[i] = random.random()

    # Print the values, one per line.
    for value in value_list:
        print(value)
