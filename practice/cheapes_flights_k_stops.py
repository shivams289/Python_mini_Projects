class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # bellman ford
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tempprices = prices.copy()
            for fr, to, price in flights:
                if prices[fr] == float("inf"):
                    continue
                if prices[fr] + price < tempprices[to]:
                    tempprices[to] = prices[fr] + price

            prices = tempprices

        return -1 if prices[dst] == float("inf") else prices[dst]
