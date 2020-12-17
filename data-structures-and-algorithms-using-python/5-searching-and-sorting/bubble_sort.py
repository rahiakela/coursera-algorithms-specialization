def bubble_sort(values):
    """Sorts a sequence in ascending order using the bubble sort algorithm."""
    n = len(values)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1):
        # Bubble the largest item to the end.
        for j in range(n - 1, i, - 1):
            # swap the j and j+1 items.
            if values[j] < values[j - 1]:
                # swap the j and j+1 items.
                tmp = values[j]
                values[j] = values[j - 1]
                values[j - 1] = tmp
    return values


if __name__ == "__main__":
    lists = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print(lists)
    lists = bubble_sort(lists)
    print(lists)
