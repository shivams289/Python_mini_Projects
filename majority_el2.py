class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <=2:
            if len(list(set(nums))) <=1:
                return list(set(nums))
            else:
                return nums
        
        nums.sort()
        new_list = list(set(nums))
        new_list.sort()
        maj = len(nums)/3
        ans = []
        for el in new_list:
            count = 0
            for nl in nums:
                if el == nl:
                    count += 1
                else:
                    break
            if count > maj:
        
                ans.append(el)
            nums = nums[count:]
        return ans
        #2nd Way