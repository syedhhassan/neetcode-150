class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, rows - 1
        while left <= right:
            midRow = (left + right) // 2
            
            if matrix[midRow][-1] < target:
                left = midRow + 1
            elif matrix[midRow][0] > target:
                right = midRow - 1
            else:
                break
        
        low, high = 0, len(matrix[midRow]) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[midRow][mid] < target:
                low = mid + 1
            elif matrix[midRow][mid] > target:
                high = mid - 1
            else:
                return True

        return False