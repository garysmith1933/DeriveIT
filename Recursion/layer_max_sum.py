def layerMaxSum(root):
    res = 0
    max_val = float('-inf')
    queue = deque([(root, 1)])

    while queue:
        layer_val = 0
        for _ in range(len(queue)):
            node, curr_layer = queue.popleft()
            
            layer_val += node.val

            if node.left: queue.append((node.left, curr_layer + 1))
            if node.right: queue.append((node.right, curr_layer + 1))
        
        if layer_val > max_val:
            max_val = layer_val
            res = curr_layer
        
    return res


    #Time O(N)
    #Space O(N)