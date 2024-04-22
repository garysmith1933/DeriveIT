def kthSmallestElementBST(root, k):
    c = 1
    solution = None

    def dfs(node):
        nonlocal c, solution

        if not node or solution != None:
            return 
        
        left = dfs(node.left)

        if c == k:
            solution = node.val
        
        c += 1

        right = dfs(node.right)
    
    
    dfs(root)
    return solution

    # Time O(k)
    # Space O(k)