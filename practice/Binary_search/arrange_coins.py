# summation of n terms n*n+1/2
class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2

            x = mid * (mid + 1) // 2
            if x == n:
                return mid
            elif x > n:
                high = mid - 1

            else:
                low = mid + 1

        return high
