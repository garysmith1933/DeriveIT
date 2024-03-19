def treeDiameter(root):
    diameter = float('-inf')
    
    def depth(root):
        if not root:
            return 0
        
        left = depth(root.left)
        right = depth(root.right)

        nonlocal diameter 
        diameter = max(left + right, diameter)

        return 1 + max(left, right)
        
   
    depth(root)
    return diameter

#Time O(N)
#Space O(N)