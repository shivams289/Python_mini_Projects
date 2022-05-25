
tab = [[-1 for i in range(2000)] for j in range(2000)]
def subset_sum(arr, n, sum_):
	if sum_ == 0:
		return 1
	if n <= 0:
		return 0

	

    if (tab[n - 1][sum_] != -1):
    	return tab[n - 1][sum_]

    if (a[n - 1] > sum_):
        tab[n - 1][sum_] = subset_sum(a, n - 1, sum_)
        return tab[n - 1][sum_]
    else:
    	tab[n - 1][sum_] = subset_sum(a, n - 1, sum_)
        return tab[n - 1][sum_] or subset_sum(a, n - 1, sum_ - a[n - 1])

