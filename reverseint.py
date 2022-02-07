def reverse(x):
    x = str(x)
    sign = 1
    if int(x)< 0:
        sign = -1
        x = x[1:]
   
    if len(x) == 1:
        return sign*int(x)

    n = len(x)
    j = ''
    for i in range(n-1, -1, -1):
        j = j + x[i]
        
    if int(j) > 2 << 31 - 1:
        return 0

    return sign*int(j)

print(reverse(-120))