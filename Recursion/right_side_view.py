def rightSideView(root): # the right most node is always the last element in the queue.
    queue = deque([root])
    res = []

    while queue:
        res.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.popleft()

            if not node:
                continue

            queue.append(node.left)
            queue.append(node.right)
            
    
    return res

    # Time O(N)
    # Space O(N)