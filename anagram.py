def isAnagram(s, t):
    if (len(s) != len(t)):
        return False
    sdic = {}
    tdic = {}
    for i in range(len(s)):
        if s[i] not in sdic.keys():
            sdic[s[i]] = 1
        else:
    	    sdic[s[i]] += 1

    for i in range(len(t)):
        if t[i] not in tdic.keys():
    	    tdic[t[i]] = 1
        else:
    	    tdic[t[i]] += 1
            
    for key in sdic.keys():
        if key not in tdic.keys():
            return False
        else:
            if tdic[key] != sdic[key]:
                return False
            
    return True