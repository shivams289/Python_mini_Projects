def ispal(s, l, r):
	if l>= r:
		return True
	if s[l] != s[r]:
		return False

	return ispal(s, l+1, r-1)
s = 'abbab'
print(ispal(s, 0, len(s)-1))