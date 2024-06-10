def lowestEnergyPath(root):
    res = []
    heap = [(root.val, 0)] # (root.val, root) 


    nodeIds = { 0 : root }
    nextId = 1 

    while heap:
        node_val, ID = heapq.heappop(heap) # instantly pops minimum
        res.append(node_val)

        node = nodeIds[ID]
        if node.left:
            nodeIds[nextId] = node.left
            heapq.heappush(heap, (node.left.val, nextId))
            nextId += 1

        if node.right:
            nodeIds[nextId] = node.right
            heapq.heappush(heap, (node.right.val, nextId))
            nextId += 1


    return res

    #Time O(N log n) - every node gets popped off the tree, which is log n, we do this n times.
    # Space O(N)