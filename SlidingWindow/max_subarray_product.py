def maxSubarrayProduct(nums):
    maxProd = arr[0]
    minProd = arr[0]
    maxSeen = maxProd

    for in range(1, len(arr)):
        curr = arr[i]

        maxProd, minProd = (
            max(maxProd*curr, minProd*curr, curr),
            min(maxProd*curr, minProd*curr, curr)
        )

        maxSeen = max(maxSeen, maxProd)
    
    return maxSeen
    
    # Time O(N)
    # Space O(1)