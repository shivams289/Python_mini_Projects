def search(a, key):
	low = 0
	high = len(a) -1
	while low <= high:
		mid = (low+high)//2
		if a[mid] == key:
			return mid
#left part sorted ----
		if a[low] < a[mid]:
			if key >= a[low] and key < a[mid]:
				high = mid -1

			else:
				low = mid +1
#right part sorted ----
		else:
			if key > a[mid] and key <= a[high]:
				low = mid + 1

			else:
				high = mid -1 
	return -1


a = [20, 30, 40, 50, 60, 5, 10]
index = search(a, 10)
print('Found_index-->', index)