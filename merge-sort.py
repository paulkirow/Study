def mergeSort(arr):
    if len(arr) < 2:
        return

    mid = len(arr) // 2

    l = arr[:mid]
    r = arr[mid:]
    print(str(l) + ":" + str(r) + "\t mid=" + str(mid) + "\t\t" + str(arr))
    mergeSort(l)
    print(str(l) + ":" + str(r) + "\t left sorted \t" + str(arr))
    mergeSort(r)
    print(str(l) + ":" + str(r) + "\t right sorted \t" + str(arr))
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        elif r[j] < l[i]:
            arr[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1


if __name__ == '__main__':
    test1 = [9, 4, 3, 2, 1, 0]
    test2 = [1]
    test3 = []
    test4 = [1, 3, 2, 6, 4]
    mergeSort(test1)
    print(test1)
    print()
    print()
    mergeSort(test2)
    print(test2)
    print()
    print()
    mergeSort(test3)
    print(test3)
    print()
    print()
    mergeSort(test4)
    print(test4)
    print()
    print()
