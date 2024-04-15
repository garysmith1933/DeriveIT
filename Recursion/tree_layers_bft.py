def treeLayers(root):
    queue = deque([root])
    res = []

    while queue:
        layer = []
        for _ in range(len(queue)):
            node = queue.popleft()
            layer.append(node.val)

            if node.left:
                queue.append(node.left)
        
            if node.right:
                queue.append(node.right)
    
        res.append(layer)

    return res
            
# Time O(N)   
# Space O(N)  