def best_time(a):
	maxprofit = 0
	minsofar = a[0]

	for val in a:
		minsofar = min(minsofar, val)
		maxprofit = max(maxprofit, val - minsofar)

	return maxprofit

def best_time_multiple_buy_sell(a):
	profit = 0

	for i in range(1, len(a)):
		if a[i] > a[i-1]:
			profit += a[i] - a[i-1]

	return profit

print(best_time([7,1,5,3,6,4]))
print(best_time_multiple_buy_sell([7,1,5,3,6,4]))