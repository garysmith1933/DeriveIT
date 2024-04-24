clones = {}

def cloneGraph(node):
    if node in clones:
        return clones[node]
    
    cloneNode = GraphNode(node.val)
    clones[node] = cloneNode
    
    for neighbor in node.neighbors:
        cloneNode.neighbors.append(cloneGraph(neighbor))
    
    return cloneNode

    # Time O(N)
    # Space O(N)
