class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            x = len(nums) - mid
            if nums[mid] >= x:
                if mid == 0 or nums[mid - 1] < x:
                    return x
                else:
                    high = mid - 1

            else:
                low = mid + 1

        return -1
