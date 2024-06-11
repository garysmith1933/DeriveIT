def merge(arr1, arr2):
    i, j = 0, 0
    res = []

    while i != len(arr1) and j != len(arr2):

        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        
        else:
            res.append(arr2[j])
            j += 1
    
    res.extend(arr1[i:])
    res.extend(arr2[j:])

    return res

def mergeSort(arr):

    if len(arr) == 0 or len(arr) == 1:
        return arr

    mid = (len(arr) - 1) // 2
    
    left = mergeSort(arr[:mid + 1]) # includes the mid point
    right = mergeSort(arr[mid + 1:]) # doesnt include mid point
    

    return merge(left, right)

# Time O(n log n)
# Space O(N)