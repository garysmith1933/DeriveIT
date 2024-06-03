def maxSubarrayProduct(nums):
    maxProd = nums[0]
    minProd = nums[0]
    maxSeen = maxProd

    for i in range(1, len(nums)):
        curr = nums[i]

        maxProd, minProd = (
            max(maxProd*curr, minProd*curr, curr),
            min(maxProd*curr, minProd*curr, curr)
        )

        maxSeen = max(maxSeen, maxProd)
    
    return maxSeen
    
    # Time O(N)
    # Space O(1)