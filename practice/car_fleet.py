class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tp = zip(position, speed)
        tp = [[x, y] for x, y in tp]
        stack = []
        for p, s in sorted(tp)[::-1]:  # reversee sorted
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # decreasing a car, makes a car fleet

        return len(stack)
