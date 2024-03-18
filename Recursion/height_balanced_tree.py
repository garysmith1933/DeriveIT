def heightBalanced(root):
    balanced = True

    def height(node):
        if not node:
            return 0
        
        heightL = height(node.left)
        heightR = height(node.right)

        if abs(heightL - heightR) > 1:
            nonlocal balanced
            balanced = False
        
        return 1 + max(heightL, heightR)

    height(root)
    return balanced
    #Time O(N)
    #Space O(N)
