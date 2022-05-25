import heapq


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums_ = []
        ans = []
        heapq.heapify(sums_)
        for i in range(len(mat)):
            heapq.heappush(sums_, (sum(mat[i]), i))

        while k > 0:
            val, index = heapq.heappop(sums_)

            ans.append(index)
            k -= 1

        return ans
