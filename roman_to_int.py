class Solution:
    def romanToInt(self, s: str) -> int:
        def value(string):
            if string == 'M':
                num = 1000
            elif string == 'D':
                num = 500
            elif string == 'C':
                num = 100

            elif string == 'L':
                num = 50

            elif string == 'X':
                num = 10

            elif string == 'V':
                num = 5

            elif string == 'I':
                num = 1
            return num
        n = len(s)
        ans = 0
        for i in range(n-1):
            if value(s[i]) >= value(s[i+1]):
                ans += value(s[i])
            else:
                ans -= value(s[i])
                
        return ans+value(s[n-1])
                
        
           