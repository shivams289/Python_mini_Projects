def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s)

    for i in range(n-1, -1 ,-1):
        s.append(s[i])
        
    for i in range(n):
        s.pop(0)