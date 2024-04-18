def smallestElement(arr):
    i, j = 0, len(arr) - 1

    while True:
        if j == i:
            return arr[i]
        
        mid = ( i + j ) // 2
        
        if arr[mid] <= arr[j]:
            j = mid
        else:
            i = mid + 1
    
    # Time O (log n)
    # Space O(1)