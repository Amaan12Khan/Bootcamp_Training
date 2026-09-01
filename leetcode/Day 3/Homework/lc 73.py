class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        # Create empty checklists filled with False
        row_checklist = [False] * num_rows
        col_checklist = [False] * num_cols
        
        # Step 2: Fill the checklists
        for r in range(num_rows):
            for c in range(num_cols):
                if matrix[r][c] == 0:
                    row_checklist[r] = True
                    col_checklist[c] = True
                    
        # Step 3: Use the checklists to update the matrix
        for r in range(num_rows):
            for c in range(num_cols):
                if row_checklist[r] or col_checklist[c]:
                    matrix[r][c] = 0
