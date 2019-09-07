def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)


def partition(arr, low, high):
    # Take last element as partition
    p = arr[high]
    i = low - 1  # index after low
    for j in range(low, high):
        if arr[j] < p:
            # current element smaller then pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(str(arr[low:i+1]) + " :" + str(p) + ": " + str(arr[i+2:high+1]) + "\t i+1=" + str(i+1)+ "\t low=" + str(low)+ "\t high=" + str(high)+ "\t arr=" + str(arr))
    return i + 1

if __name__ == '__main__':
    test1 = [1, 3, 2, 6, 4, 9, 5]
    test2 = [1]
    test3 = []
    test4 = [9, 4, 3, 2, 1, 0]
    #quickSort(test1, 0, len(test1)-1)
    #quickSort(test2, 0, len(test2)-1)
    #quickSort(test3, 0, len(test3)-1)
    quickSort(test4, 0, len(test4)-1)
    print(test1)
    print(test2)
    print(test3)
    print(test4)
