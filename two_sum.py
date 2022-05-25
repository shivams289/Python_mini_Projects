# two sum 2: Leetcode problem
class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        l, r = 0, n - 1
        for i in range(n):
            while numbers[l] + numbers[r] != target:
                if numbers[l] + numbers[r] > target:
                    r -= 1
                else:
                    l += 1

            return [l + 1, r + 1]


# Two sum leetcode problem
class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        dic = dict()
        for i, val in enumerate(nums):
            check = target - val
            if check in dic:
                return [i, dic[check]]
            else:
                dic[val] = i
