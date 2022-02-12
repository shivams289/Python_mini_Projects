def swap(a, x, y):
	temp =  a[x]
	a[x] = a[y]
	a[y] = temp

#check if a element is smaller than its previous, if it is then swap, 
#since the largest elemnt will be placed at its posiiton will each iteration ..you need to look
#only before than range of elements
def bubbleSort(a):
	swaped = False
	for i in range(len(a)):
		for j in range(len(a)-i-1):
			if a[j+1] < a[j]:
				swaped = True
				swap(a, j+1, j)
		if swaped == False:
			break

	return a


a = [4, 3, 7, 1, 5]
print(bubbleSort(a))