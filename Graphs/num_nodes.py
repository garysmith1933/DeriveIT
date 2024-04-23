# def numNodes(node):
#     visited = set()

#     def countNodes(node):
#         nonlocal visited

#         if node in visited:
#             return
        
#         visited.add(node)

#         for neighbor in node.neighbors:
#             countNodes(neighbor)
    
#     countNodes(node)
#     return len(visited)

#     # Time O(N)
#     # Space O(N)

visited = set()

def numNodes(node):
    if node in visited:
            return 0
        
    visited.add(node)

    return 1 + sum(numNodes(neighbor) for neighbor in node.neighbors)

    # Time O(N)
    # Space O(N)