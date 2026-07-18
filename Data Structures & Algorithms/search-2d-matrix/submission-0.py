class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])
        flattened_mat = []
        for i in range(row):
            for j in range(col):
                flattened_mat.append(matrix[i][j])

        left = 0
        right = row*col-1

        while left <= right:
            mid = (left+right) // 2
            if flattened_mat[mid] == target:
                return True
            
            elif flattened_mat[mid] < target:
                left = mid + 1
            
            elif flattened_mat[mid] > target:
                right = mid - 1
        
        return False