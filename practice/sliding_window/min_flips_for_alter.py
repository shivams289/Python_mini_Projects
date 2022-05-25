class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        alt1, alt2 = "", ""
        s = s + s
        for i in range(len(s)):
            alt1 += "0" if i % 2 == 0 else "1"
            alt2 += "1" if i % 2 == 0 else "0"

        dif1, dif2 = 0, 0
        left = 0
        res = len(s)
        for right in range(len(s)):
            if s[right] != alt1[right]:
                dif1 += 1

            if s[right] != alt2[right]:
                dif2 += 1

            if (right - left + 1) > n:
                if s[left] != alt1[left]:
                    dif1 -= 1

                if s[left] != alt2[left]:
                    dif2 -= 1

                left += 1

            if (right - left + 1) == n:
                res = min(dif1, dif2, res)

        return res
