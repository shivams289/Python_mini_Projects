class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        if len(nums) == 1:
            return 0
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1

        return low
