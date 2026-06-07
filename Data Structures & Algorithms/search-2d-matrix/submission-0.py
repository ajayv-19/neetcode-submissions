from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  
            return False  # Edge case: empty matrix
        
        m, n = len(matrix), len(matrix[0])  # Rows and columns
        left, right = 0, m * n - 1  # Binary search on the "flattened" matrix
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = matrix[mid // n][mid % n]  # Convert 1D index to 2D
            
            print(f"Searching at index: {mid} -> matrix[{mid // n}][{mid % n}] = {mid_value}")

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
