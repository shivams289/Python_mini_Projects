class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            premap[c].append(p)

        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if premap[crs] == []:
                return True
            cycle.add(crs)

            for pre in premap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            premap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
