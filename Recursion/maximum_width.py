def maximumWidth(root): # hint (nodes are numbered 0, 1, 2)
    maxWidth = float('-inf')
    queue = deque([(root,0)])

    while queue:
        _, nL = queue[0] # left most
        _, nR = queue[-1] # right most

        width = nR - nL + 1
        maxWidth = max(maxWidth, width)

        for _ in range(len(queue)):
            node, n = queue.popleft()
            
            if node.left: queue.append((node.left, 2 * n))
            if node.right: queue.append((node.right, 2*n + 1))
        
    
    return maxWidth
# Time O(N)
# Space O(N)