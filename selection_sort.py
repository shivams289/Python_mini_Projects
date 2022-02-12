def swap(a, index, i):
    temp = a[i]
    a[i] = a[index]
    a[index] = temp
def selectionSort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            swap(arr, min_index, i)

  

arr = [12, 11, 13, 5, 6]
selectionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])