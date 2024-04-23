def numNodes(node):
    visited = set()

    def countNodes(node):
        nonlocal visited

        if node in visited:
            return
        
        visited.add(node)

        for neighbor in node.neighbors:
            countNodes(neighbor)
    
    countNodes(node)
    return len(visited)

    # Time O(N)
    # Space O(N)s