def packageInstaller(root):
    res = []

    def dfs(node):
        if not node:
            return None
        
        res.append(node.val)

        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return res