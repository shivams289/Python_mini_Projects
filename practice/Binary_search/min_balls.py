class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        low = 1
        high = max(nums)
        ans = high

        while low <= high:
            reqop = 0
            maxsize = (low + high) // 2
            for num in nums:
                op = (num - 1) // maxsize
                reqop += op
            if reqop <= maxOperations:
                high = maxsize - 1
                ans = maxsize
            else:
                low = maxsize + 1

        return ans
