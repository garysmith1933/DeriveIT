def maxSubtreeSum(root):
    maxSum = float('-inf')

    def get_sum(root):
        if root is None:
            return 0
        
        current_sum = root.val + get_sum(root.left) + get_sum(root.right)

        nonlocal maxSum
        maxSum = max(current_sum, maxSum)

        return current_sum     
    
    get_sum(root)
    return maxSum
#Time O(N)
#Space O(N)
