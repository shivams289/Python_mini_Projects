class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        for i, el in enumerate(nums):
            if i > 0 and el == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                sum_ = el + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1

                else:
                    ans.append([el, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return ans
