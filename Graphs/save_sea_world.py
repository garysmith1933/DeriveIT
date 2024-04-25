def saveSeaWorld(height):
    m, n = len(height), len(height[0])

    river = [[False for _ in range(n)] for _ in range(m)]
    bay = [[False for _ in range(n)] for _ in range(m)]

    def reachable(matrix, row, col):
        matrix[row][col] = True

        for r,c in [(row + 1, col), (row - 1, col) (row, col + 1), (row, col - 1)]:
            if 0 <= r < m and 0 <= c < n and height[row][col] <= height[r][c] and not matrix[r][c]:
                reachable(matrix, r, c)
        

    for row in range(m):
        reachable(bay, row, 0)
        reachable(river, row, n - 1) # right side of river
        for col in range(n):
            reachable(bay, 0, col)
            reachable(river, m - 1, col)
    
    return [
        [r,c] for r in range(m) for c in range(n) if river[r][c] and bay[r][c]
    ]
    