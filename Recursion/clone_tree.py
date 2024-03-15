def cloneTree(root):
    if not root:
        return None
    
    copyNode = TreeNode(root.val)
    copyNode.left = cloneTree(root.left)
    copyNode.right = cloneTree(root.right)

    return copyNode

    # Time O(N)
    # Space O(N)