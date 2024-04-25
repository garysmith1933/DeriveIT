def numChocolateChips(matrix):
    n = len(matrix)
    m = len(matrix[0])

    def processChip(row, col):
        matrix[row][col] = 0 

        for r,c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
        
            if 0 <= r < n and 0 <= c < m and matrix[r][c] == 1:
                processChip(r, c)

    count = 0 
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 1:
                count += 1
                processChip(row, col)
    
    return count

    # Time O(nm)
    # Space O(nm)