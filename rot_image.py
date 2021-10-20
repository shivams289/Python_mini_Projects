class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        final = []
        for i in range(n):
            lst = []
            for j in range(n):
                lst.append(matrix[n-1-j][i])
            final.append(lst)
            
        for i in range(n):
            for j in range(n):
                matrix[i][j] = final[i][j]