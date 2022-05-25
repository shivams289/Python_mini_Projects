def binary_search(n, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if n != 0 and arr[mid] == n:
            return True
        elif arr[mid] > n:
            high = mid - 1

        else:
            low = mid + 1
    return False


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        if arr.count(0) > 1:
            return True

        for i, el in enumerate(arr):
            if binary_search(2 * el, arr):
                return True

        return False
