def odd_occurring(arr, arr_size):
    for i in range(0, arr_size):
        count = 0
        for j in range(0, arr_size):
            if arr[i] == arr[j]:
                count += 1
        if count % 2 != 0:
            return arr[i]
    return -1


if __name__ == "__main__":
    arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
    n = len(arr)
    print(odd_occurring(arr, n))

    arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 4]
    n = len(arr)
    print(odd_occurring(arr, n))
