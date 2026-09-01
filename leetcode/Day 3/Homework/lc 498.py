class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
    
        diagonals = defaultdict(list)
        m, n = len(mat), len(mat[0])
    
    # Step 1: Group all elements by their diagonal sum (i + j)
        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])
            
        result = []
    
    # Step 2: Merge diagonals, reversing the even-indexed groups
        for k in range(m + n - 1):
            if k % 2 == 0:
                result.extend(diagonals[k][::-1])  # Reverse for up-right direction
            else:
                result.extend(diagonals[k])        # Keep natural down-left order
            
        return result
