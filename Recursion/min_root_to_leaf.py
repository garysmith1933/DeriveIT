def minLength(root):
    if not root:
        return float('inf')
    
    if not root.left and not root.right:
        return 1

    left = minLength(root.left)
    right = minLength(root.right)

    return 1 + min(left, right)
    
    #Time O(N)
    #Space O(N)