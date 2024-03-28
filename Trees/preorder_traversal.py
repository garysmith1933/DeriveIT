def preorderArray(root):
    res = []

    def dfs(node):
        if not node:
            return 
        
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res

# Time O(N)
# Space O(N) - call stack grows to depth of the tree, which could be n nodes deep