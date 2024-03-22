def maximumLeafSum(root):
    if not root:
        return float('-inf')
    
    if not root.left and not root.right:
        return root.val

    left = maximumLeafSum(root.left)
    right = maximumLeafSum(root.right) 

    root.val = root.val + max(left, right)

    return root.val
    
    # Time O(N)
    # Space O(N)