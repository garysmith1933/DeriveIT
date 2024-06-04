def threeSum(arr, target):
    seen = set([])

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            a = arr[i]
            b = arr[j]

            c = target - a - b

            if c in seen:
                return True
            
        seen.add(a)
    
    return False

    # Time O(N*2)
    # Space O(N)