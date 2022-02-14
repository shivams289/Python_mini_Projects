def iterative_binary_search(a, key):
	low = 0
	high = len(a)-1
	while(low <= high):
		mid = (low + high)//2
		if a[mid] == key:
			return mid

		elif key > a[mid]:
			low = mid + 1

		else:
			high = mid - 1

	return -1
def Search_infinite(a, key):
	low = 0
	high = 1
	while(a[high] < key):
		low = high
		high = high <<1

	return iterative_binary_search(a, key, low, high)