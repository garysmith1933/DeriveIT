def invertAll(root):
    if not root: 
        return 
    
    root.left, root.right = root.right, root.left

    invertAll(root.left)
    invertAll(root.right)

    #Time O(N)
    #Space O(N)