def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                array[j],array[j + 1] = array[j + 1],array[j]



myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(myList)
print("Bubble Sorted Array: ", myList)