def postorderTraversal(root):
    res = []

    stack = [(root, True)]

    while stack:
        node, isFirstCall = stack.pop()
    
        if not node:
            continue

        if isFirstCall:
            stack.append((node, False))
            stack.append((node.right, True))
            stack.append((node.left, True))

        else:
            res.append(node.val)
    
    return res

# Time O(N)
# Space O(N)