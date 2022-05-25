class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        set1 = list(set(nums1))
        set2 = list(set(nums2))

        if len(set1) >= len(set2):
            return list(set(set1) - (set(set1) - set(set2)))

        else:
            return list(set(set2) - (set(set2) - set(set1)))
