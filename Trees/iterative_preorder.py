def preorderTraversal(root):
    res = []

    stack = [root]

    while stack:
        node = stack.pop()
    
        if not node:
            continue

        res.append(node.val)
        stack.append(node.right)
        stack.append(node.left)
        
    
    return res

# Time O(N)
# Space O(N)