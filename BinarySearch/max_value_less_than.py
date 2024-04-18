def maxValueLessThan(arr, high):
    i, j = 0, len(arr) - 1
    largest = None

    while True:
        if j == i - 1:
            return largest
        
        mid = (i + j) // 2

        if arr[mid] < high: 
            largest = arr[mid]
            i = mid + 1
        
        else:
            j = mid - 1
    
    return largest

    #Time O(log n)
    #Space O(1)