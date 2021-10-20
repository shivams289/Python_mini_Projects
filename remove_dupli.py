class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        for el in nums:
            if el not in res:
                res.append(el)
        for i in range(len(res)):
            nums[i] = res[i]
               
        return len(res)
        