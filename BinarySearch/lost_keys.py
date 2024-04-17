def timeLost(video):
    i, j = 0, len(video) - 1
    leftmost = None

    while True:
        if j == i - 1:
            return leftmost
        
        mid = ( i + j ) // 2

        if video[mid]:
            i = mid + 1
        else:
            leftmost = mid
            j = mid - 1

    
    return leftmost
    
    # Time O(log n)
    # Space O(1)