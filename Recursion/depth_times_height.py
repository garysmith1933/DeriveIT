def depthTimesHeight(root):

    def dfs(node, depth):
        if not node:
            return 0

        left = dfs(node.left, depth + 1)
        right = dfs(node.right, depth + 1)

        height = 1 + max(left, right)

        node.val = height * depth

        return height 
    
    dfs(root, 1)

    # Time O(N)
    # Space O(N)