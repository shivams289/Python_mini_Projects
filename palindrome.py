def isPalindrome(s):
    import re
    s = re.sub('[^a-zA-Z0-9]', '', s)
    s = s.lower()
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True