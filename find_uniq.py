def firstUniqChar( s):
    dic ={}

    for i in range(len(s)):
        if s[i] not in dic.keys():
            dic[s[i]] = 1

        else:
            dic[s[i]] +=1
            
    val = ''
    for key in dic.keys():
        if dic[key] == 1:
            val = key
            break
    for i in range(len(s)):
        if val == s[i]:
            return i
    return -1