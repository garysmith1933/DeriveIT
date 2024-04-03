def rightmostLocation(root, location=0):
    if not root:
        return float('-inf')
    
    if not root.left and not root.right:
        return location 
    
    left = rightmostLocation(root.left, location - 1)
    right = rightmostLocation(root.right, location + 1)

    return max(left, right)

    #Time O(N)
    #Space O(N)