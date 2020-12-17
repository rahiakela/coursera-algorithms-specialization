def binary_search(values, target):
    """Implementation of the binary search algorithm."""

    # Start with the entire sequence of elements.
    low = 0
    high = len(values) - 1

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        # Find the midpoint of the sequence.
        mid = (high + low) // 2
        # Does the midpoint contain the target?
        if values[mid] == target:
            return True
        elif target < values[mid]:  # Or does the target precede the midpoint?
            high = mid - 1
        elif target > values[mid]:
            low = mid + 1
        else:  # Or does it follow the midpoint?
            low = high + 1
    # If the sequence cannot be subdivided further, we're done.
    return False


def find_sorted_position(values, target):
    """
    Modified version of the binary search that returns the index within
    a sorted sequence indicating where the target should be located.
    """
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (high + low) // 2
        if values[mid] == target:
            return mid   # Index of the target.
        elif target < values[mid]:
            high = mid - 1
        else:
            low = mid + 1
    # Index where the target value should be.
    return low


if __name__ == "__main__":

    lists = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]

    # Searching for 10
    print("Found: ", binary_search(lists, 10))

    # Searching for 18
    print("Found: ", binary_search(lists, 18))



