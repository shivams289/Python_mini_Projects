def myAtoi(self, s: str) -> int:
    sx = re.sub('[^a-zA-Z0-9]', '', s)
    if not (sx[0].isdigit()):
        return 0
        
    
    neg = 1
    if '-' in s:
        neg = -1
    s = re.sub('[^0-9.]', '', s)
    s = s.lower()
    ans = neg*int(float(s))
    
    if ans>(2**31 - 1):
        return (2**31 - 1)
    if ans<-2**(31):
        return -2**(31)
    
    return ans
    