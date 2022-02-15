#find the subarray with the given sum

def subarraysum(a, sum_):
	cursum = 0
	start = 0
	end = -1
	n = len(a)
	dic = dict()

	for i in range(n):
		cursum += a[i]
		if cursum == sum_:
			start = 0
			end = i
			break

		if (cursum - sum_) in dic.keys():
			start = dic[cursum - sum_] +1
			end = i
			break

		dic[cursum] = i

	if end == -1:
		print('Not_found')
	else:
		print(f'start:{start} and end:{end}')

a = [10, 15, -5, 15, -10, 5]
#cursum = [10, 25, 20, 35, 25, 30]

subarraysum(a, 5)