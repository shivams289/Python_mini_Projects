class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        union = []
        
        def check(el, nums):
            for i,e in enumerate(nums):
                if el == e:
                    nums.pop(i) #Important to remove element that has already been included
                    return True
            return False
                
        if n1>=n2:
            for el in nums2:
                if check(el, nums1):
                    union.append(el)
        else:
            for el in nums1:
                if check(el, nums2):
                    union.append(el)
        
            
                    
        return union
            
                    
                
            
        