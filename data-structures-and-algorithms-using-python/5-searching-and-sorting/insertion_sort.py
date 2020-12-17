def insertion_sort(values):
    """Sorts a sequence in ascending order using the insertion sort algorithm."""
    n = len(values)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned.
        value = values[i]
        # Find the position where value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value < values[pos - 1]:
            # Shift the items to the right during the search.
            values[pos] = values[pos - 1]
            pos -= 1
        # Put the saved value into the open slot.
        values[pos] = value
    return values


if __name__ == '__main__':
    lists = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print(lists)
    lists = insertion_sort(lists)
    print(lists)
