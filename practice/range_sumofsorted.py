class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        lst = []
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                lst.append(curr)

        lst.sort()

        return sum(lst[left - 1 : right]) % (10**9 + 7)
