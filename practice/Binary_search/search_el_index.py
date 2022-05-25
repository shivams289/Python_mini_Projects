class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        low = 0
        high = len(nums) - 1
        ans = []
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                k = mid - 1
                while k >= 0 and nums[k] == target:
                    ans.append(k)
                    k -= 1

                ans.sort()
                ans.append(mid)
                k = mid + 1
                while k <= len(nums) - 1 and nums[k] == target:
                    ans.append(k)
                    k += 1
                return ans
            else:
                if nums[mid] > target:
                    high = mid - 1

                else:
                    low = mid + 1

        return []
