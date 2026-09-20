class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, (len(matrix)) * (len(matrix[0])) - 1

        while left <= right:
            mid = int((left + right) / 2)
            midCol = int(mid % len(matrix[0]))
            midRow = int(mid / len(matrix[0]))

            if matrix[midRow][midCol] < target:
                left = mid + 1
            elif matrix[midRow][midCol] > target:
                right = mid - 1
            elif matrix[midRow][midCol] == target:
                return True
            
        return False