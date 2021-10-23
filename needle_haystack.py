def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) == 0 :
        return 0
    elif len(haystack) == 0:
        return -1
    
    elif len(needle)==1 and len(haystack)==1:
        if needle in haystack:
            return 0
    elif needle in haystack:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
    else:
        return -1