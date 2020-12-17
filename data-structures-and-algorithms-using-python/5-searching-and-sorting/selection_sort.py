def selection_sort(values):
    """Sorts a sequence in ascending order using the selection sort algorithm."""
    n = len(values)
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallest_idx = i
        # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if values[j] < values[smallest_idx]:
                smallest_idx = j
        """ 
        Swap the ith value and smallest idx value only if the smallest value is
        not already in its proper position. Some implementations omit testing
        the condition and always swap the two values.
        """
        if smallest_idx != i:
            tmp = values[i]
            values[i] = values[smallest_idx]
            values[smallest_idx] = tmp
    return values


if __name__ == '__main__':
    lists = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print(lists)
    lists = selection_sort(lists)
    print(lists)
