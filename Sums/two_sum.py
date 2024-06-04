def twoSum(arr, target):
    
    seen = set([])

    for num in arr:
        other = target - num

        if other in seen:
            return True
        
        seen.add(num)
    
    return False
    
    # Time O(N)
    # Space O(N)