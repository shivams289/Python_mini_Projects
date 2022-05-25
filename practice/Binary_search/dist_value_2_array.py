class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        [1, 8, 9, 10]
        count = 0
        arr2.sort()
        for el in arr1:
            res = False
            left, right = 0, len(arr2) - 1

            print(el)
            while left <= right:
                mid = (left + right) // 2
                if abs(arr2[mid] - el) <= d:
                    res = True
                    break

                elif arr2[mid] > el:
                    right = mid - 1

                else:
                    left = mid + 1

            if res == True:
                count += 1

        return len(arr1) - count
