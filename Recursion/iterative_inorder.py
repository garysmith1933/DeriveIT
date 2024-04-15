def inorderTraversal(root): # left, node, right
# visit each node twice to process the left, then process the node, then the right.
    res = []

    stack = [(root, True)]

    while stack:
        node, isFirstCall = stack.pop()
    
        if not node:
            continue

        if isFirstCall:
            stack.append((node.right, True))
            stack.append((node, False))
            stack.append((node.left, True))

        else:
            res.append(node.val)
    
    return res

# Time O(N)
# Space O(N)