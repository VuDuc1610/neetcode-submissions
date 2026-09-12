class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        while l <= r:
            mid = l + (r-l)//2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                i,j = 0, len(matrix[0])
                while i <= j:
                    m = i + (j-i)//2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        i = m + 1
                    else:
                        j = m - 1
                return False
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False