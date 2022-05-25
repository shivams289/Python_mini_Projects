class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        res = 0
        maxf = 0
        left = 0
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1

            else:
                count[s[right]] = 1

            maxf = max(maxf, count[s[right]])

            if (right - left + 1) - maxf <= k:
                res = max(res, right - left + 1)
            else:
                count[s[left]] -= 1
                if not count[s[left]]:
                    count.pop(s[left])
                left += 1

        print(count)
        return res
