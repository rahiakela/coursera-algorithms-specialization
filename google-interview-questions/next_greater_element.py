def find_next_greater(arr):
    """Next Greater Element"""
    for i in range(0, len(arr), 1):
        next = -1
        for j in range(i + 1, len(arr), 1):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        print(str(arr[i]) + " -- "+ str(next))


def find_next_greater(arr, n):
    """Next greater element in same order as input"""
    s = list()

    arr1 = [0 for i in range(n)]

    # iterating from n-1 to 0
    for i in range(n - 1, -1, -1):
        # We will pop till we get the greater element on top or stack gets empty
        while len(s) > 0 and s[-1] <= arr[i]:
            s.pop()
        """
        if stack got empty means there is no element on right which is  
        greater than the current element. if not empty then the next greater  
        element is on top of stack 
        """
        if len(s) == 0:
            arr1[i] = -1
        else:
            arr1[i] = s[-1]
        s.append(arr[i])
    for i in range(n):
        print(arr[i], " ---> ", arr1[i])


if __name__ == '__main__':
    arr = [11, 13, 21, 3]
    #print(find_next_greater(arr))

    arr = [4, 5, 2, 25]
    #print(find_next_greater(arr))

    arr = [13, 7, 6, 12]
    #print(find_next_greater(arr))

    arr = [11, 13, 21, 3]
    n = len(arr)
    print(find_next_greater(arr, n))

    arr = [4, 5, 2, 25]
    n = len(arr)
    print(find_next_greater(arr, n))
