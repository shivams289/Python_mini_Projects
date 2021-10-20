class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        lst = []
        for i in range(len(nums)):
            if nums[i] == 0:
                lst.append(nums[i])
        count = 0
        for el in nums:
            if el==0:
                count+=1
        for i in range(count):
            nums.remove(0)


        for el in lst:
            nums.append(el)
                
                
                