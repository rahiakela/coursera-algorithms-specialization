def merge_sorted_lists(list_a, list_b):
    """Merges two sorted lists to create and return a new sorted list."""

    # Create the new list and initialize the list markers.
    new_list = list()
    a, b = 0, 0

    # Merge the two lists together until one is empty.
    while a < len(list_a) and b < len(list_b):
        if list_a[a] < list_b[b]:
            new_list.append(list_a[a])
            a += 1
        else:
            new_list.append(list_b[b])
            b += 1

    # If listA contains more items, append them to newList.
    while a < len(list_a):
        new_list.append(list_a[a])
        a += 1

    # Or if listB contains more items, append them to newList.
    while b < len(list_b):
        new_list.append(list_b[b])
        b += 1

    return new_list


if __name__ == '__main__':
    list_a = [2, 8, 15, 23, 37]
    list_b = [4, 6, 15, 20]
    print(list_a)
    print(list_b)
    new_list = merge_sorted_lists(list_a, list_b)
    print(new_list)
