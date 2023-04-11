def merge(arr, l, m, r):
    global global_counter

    result = [0] * (r - l + 1)

    # Merge the temp arrays back into arr[l..r]
    i = l  # Initial index of first subarray
    j = m+1 # Initial index of second subarray

    k = 0
    while i <= m and j <= r:
        if arr[i] > arr[j]:
            result[k] = arr[i]
            global_counter += i - l
            i += 1
        else:
            result[k] = arr[j]
            j += 1
        k+=1

    # Copy the remaining elements of L[], if there
    # are any
    while i <= m:
        result[k] = arr[i]
        i += 1
        k+=1


    # Copy the remaining elements of R[], if there
    # are any
    while j <= r:
        result[k] = arr[j]
        global_counter += i - l - 1
        j += 1
        k+=1

    c = 0
    for item in result:
        arr[l+c] = item
        c += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)

global_counter = 0

# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

print(*arr)
mergeSort(arr, 0, n - 1)
print(*arr)
print(global_counter)

global_counter = 0
arr3 = [1, 1, 2, 3, 4, 179]
#arr3 = [179, 4, 3, 2, 1, 1]
print(*arr3)

mergeSort(arr3, 0, n - 1)
print(*arr3)
print(global_counter)
# This code is contributed by Mohit Kumra