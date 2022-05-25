class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            capacity = (low + high) // 2
            curr = 0
            d = 1
            for w in weights:
                curr += w
                if curr > capacity:
                    curr = w
                    d += 1

            if d > days:
                low = capacity + 1

            else:
                high = capacity - 1
        return low
