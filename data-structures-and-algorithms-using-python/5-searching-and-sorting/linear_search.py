def linear_search(lists, item):
    """Finding a Specific Item"""
    n = len(lists)
    for i in range(n):
        # If the target is in the ith element, return True
        if lists[i] == item:
            return True
    # If not found, return False.
    return False


def sorted_linear_search(lists, item):
    """Searching a Sorted Sequence"""
    n = len(lists)
    for i in range(n):
        # If the target is found in the ith element, return True
        if lists[i] == item:
            return True
        elif lists[i] > item: # If target is larger than the ith element, it's not in the sequence.
            return False
    return False  # The item is not in the sequence.


def find_smallest(lists):
    """Finding the Smallest Value"""
    n = len(lists)
    # Assume the first item is the smallest value.
    smallest = lists[0]
    # Determine if any other item in the sequence is smaller.
    for i in range(1, n):
        if lists[i] < smallest:
            smallest = lists[i]
    return smallest # Return the smallest found.


if __name__ == "__main__":
    lists = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

    # Searching for 31
    print("Found: ", linear_search(lists, 31))
    # Searching for 8
    print("Found: ", linear_search(lists, 8))

    # Searching for 8
    print("Found: ", sorted_linear_search(lists, 8))

    # Searching for smallest value
    print("Found: ", find_smallest(lists))
