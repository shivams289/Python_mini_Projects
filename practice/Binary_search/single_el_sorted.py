class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Method 1
        """dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] +=1

        for x, y in dic.items():
            if y == 1:
                return x"""

        # Method 2

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = 2 * ((lo + hi) // 4)
            print(mid)
            if mid + 1 and nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]
