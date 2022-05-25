def binary_search(a):
    low = 0
    high = len(a) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        if a[mid] < 0:
            high = mid - 1

        else:
            low = mid + 1

    return len(a) - low


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            if grid[i][0] < 0:
                count += len(grid[i])

            elif grid[i][-1] > 0:
                continue

            else:
                count += binary_search(grid[i])
            print(count)

        return count
