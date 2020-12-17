def find_majority(values, n):
    max_count = 0
    index = -1

    for i in range(n):
        count = 0
        for j in range(n):
            # increment count for the same element
            if values[i] == values[j]:
                count += 1
            # update maxCount if count of current element is greater
            if count > max_count:
                max_count = count
                index = i
    # if maxCount is greater than n/2 return the corresponding element
    if max_count > n / 2:
        print(values[index])
    else:
        print("No Majority Element")


if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1]
    n = len(arr)
    find_majority(arr, n)

    arr = [1, 5, 2, 2, 3, 5, 5]
    n = len(arr)
    find_majority(arr, n)