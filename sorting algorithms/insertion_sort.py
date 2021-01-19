def insertion_sort(arr):
    for i in range(1, len(arr)):
        # Set key:
        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:
            # Swap:
            print(arr[j],arr[j+1])
            arr[j + 1] = arr[j]
            arr[j] = key

            # Decrement 'j':
            j -= 1

    return arr


array = [5, 2, 12, 41, 1]
print("Original array: %s" % array)
print("Sorted array: %s" % insertion_sort(array))