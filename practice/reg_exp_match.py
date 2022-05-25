class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:  # memoization
                return dp[(i, j)]

            if i >= len(s) and j >= len(
                p
            ):  # both ranges have been exhausted, that means both matched till now, return True
                return True

            if j >= len(p):  # if only j have exhausted that means not matched
                return False

            match = i < len(s) and (
                s[i] == p[j] or p[j] == "."
            )  # i is not exhausted and check if there's a match

            if (j + 1) < len(p) and p[j + 1] == "*":
                dp[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return dp[(i, j)]
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False

            return False

        return dfs(0, 0)
