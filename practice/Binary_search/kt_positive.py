class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        [1, 5, 6, 8, 9, 10, 11]
        missing_list = list(set([i for i in range(1, arr[-1] + 1)]) - set(arr))
        missing_list.sort()
        if len(missing_list) >= k:
            return missing_list[k - 1]

        else:
            return arr[-1] + k - len(missing_list)

        return -1
