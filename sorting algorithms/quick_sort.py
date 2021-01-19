def QuickSort(arr):
    elements = len(arr)

    if elements < 2:
        return arr

    current_position = 0

    for i in range(1, elements):
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp
    left = QuickSort(arr[0:current_position])
    right = QuickSort(arr[current_position + 1:elements])

    arr = left + [arr[current_position]] + right

    return arr


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Original Array: ", myList)
print("Quick Sorted Array: ", QuickSort(myList))
