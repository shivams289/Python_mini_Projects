#Priority que problem
import heapq
a = [2,5,4,8,6,9]
def min_cost(a):
	ans = 0
	while(len(a)>1):
		heapq.heapify(a)
		first = heapq.heappop(a)
		second = heapq.heappop(a)
		sum_ = first + second
		ans += sum_
		heapq.heappush(a, sum_)

	return ans

print('Minimum_Cost:',min_cost(a))

#Dry run

#first = 2, second = 4, sum = 6, a = [5, 6, 6, 8, 9], ans = 6
#first = 5, second = 6, sum = 11, a = [6, 8, 9, 11], ans = 17
#first = 6 , second = 8, sum = 14, a = [9, 11, 14], ans = 31
#first = 9, second = 11, sum = 20, a = [14, 20], ans = 51
#first = 14, second = 20, sum = 34, a = [34], ans = 85
