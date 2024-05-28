def maxSubarraySum(arr):
    maxSum = float('-inf')
    s = 0

    for num in arr:
        s += num
        maxSum = max(maxSum, s)

        if s < 0:
            s = 0
    
    return maxSum
    
    # Time O(n)
    # Space O(1)