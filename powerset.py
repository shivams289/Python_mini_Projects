def powerset(s , i, current):

	if i == len(s):
		print(current)
		return 
	powerset(s, i+1, current+s[i])
	powerset(s, i+1, current)

powerset('abc', 0, '')