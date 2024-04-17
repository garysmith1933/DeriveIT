# def binarySearch(arr, target): - RECURSIVE
    
#     def search(i, j):
#         if j == i - 1:
#             return None
        
#         mid = (i + j) // 2

#         if arr[mid] > target: return search(i, mid - 1)
#         if arr[mid] < target: return search(mid + 1, j)
#         if arr[mid] == target: return mid
    
#     return search(0, len(arr)-1)

    # Time O( log n)
    # Space O( log n)

def binarySearch(arr, target): # ITERATIVE
    i, j = 0, len(arr) - 1

    while True:
        if j == i - 1:
            return None 

        mid = (i + j) // 2

        if arr[mid] > target:
            j = mid - 1
        
        if arr[mid] < target:
            i = mid + 1
        
        if arr[mid] == target:
            return mid

    # Time O( log n)
    # Space O(1)