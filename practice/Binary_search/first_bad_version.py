# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            res = isBadVersion(mid)
            if res == True:
                res2 = isBadVersion(mid - 1)
                if res2 == False:
                    return mid
                else:
                    high = mid - 1

            else:
                low = mid + 1
