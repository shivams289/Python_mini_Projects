class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                if k == 0:
                    while nums[left] != 0:
                        left += 1
                    left += 1
                else:
                    k -= 1

            ans = max(ans, right - left + 1)

        return ans
