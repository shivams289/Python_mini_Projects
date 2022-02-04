
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    #1st way
        '''if len(nums)<=2:
            return nums[0]
        if len(list(set(nums))) == 1:
            return nums[0]
        
        nums.sort()
        new_list = list(set(nums))
        new_list.sort()
        maj = len(nums)/2
        for el in new_list:
            count = 0
            for nl in nums:
                if el == nl:
                    count += 1
                else:
                    break
            if count >maj:
                return el
            nums = nums[count:]'''
        #2nd Way
        nums.sort()
        return nums[len(nums)//2]
                    
                
            
        