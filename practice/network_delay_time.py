from collections import defaultdict
import heapq as hq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minheap = [(0, k)]  # edge 1 to edge1 weight is 0
        visit = set()
        t = 0
        print(edges)
        while minheap:
            w1, n1 = hq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    hq.heappush(minheap, (w1 + w2, n2))

        return t if len(visit) == n else -1
