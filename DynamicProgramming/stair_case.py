def numPaths(n):
    prev = 0
    current = 1

    for i in range(1, n + 1):
        temp = current
        current = current + prev
        prev = temp
    
    return current

    #Time O(n)
    # Space O(1)

    