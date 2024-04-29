def isPrerequisite(A, B, prerequisites, n):
    graph = {i: [] for i in range(n)}
    
    for [a,b] in prerequisites:
        graph[b].append(a)

    queue = deque([B])
    visited = set([])

    while queue:
        curr_num = queue.popleft()

        if curr_num in visited:
            continue
        
        if curr_num == A:
            return True

        visited.add(curr_num)

        for nbr in graph[curr_num]:
            queue.append(nbr)
    
    return False
    
# O(N + E) Time - N = number of courses, E = number of edges
# O(N + E) space