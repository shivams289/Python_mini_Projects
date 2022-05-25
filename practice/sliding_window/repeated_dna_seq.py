class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = dict()
        ans = []
        for left in range(len(s) - 9):
            sub = s[left : left + 10]
            if sub in res:
                res[sub] += 1
            else:
                res[sub] = 1
        for key, val in res.items():
            if val >= 2:
                ans.append(key)

        return ans
