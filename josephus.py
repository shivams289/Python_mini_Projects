#Ever kth guy will be killed clockwise, starting position of the gun is 1st person
#all sitting on a circle
#who will be saved in the end
def jos(n, k):
	if n==1:
		return 0
	return (jos(n-1, k) +k) %n

print(jos(11, 3))