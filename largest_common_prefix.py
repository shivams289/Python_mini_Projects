def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ''
    minlen = min(strs,   key =len)
    for i, el in enumerate(minlen):
        for other_el in strs:
            if other_el[i] != el:
                return minlen[:i]
    return minlen
    