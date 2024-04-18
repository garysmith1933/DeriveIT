def rotatedSearch(arr, target):
    i, j = 0, len(arr) - 1

    while True:
        if j == i - 1:
            return None
        
        mid = ( i + j ) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] <= arr[j]: 
            if arr[mid] <= target <= arr[j]:
                i = mid + 1
            else:
                j = mid - 1
        
        else:
            if arr[i] <= target <= arr[mid]:
                j = mid - 1
            else:
                i = mid + 1
    
    # Time O(log n)
    # Space O(1)