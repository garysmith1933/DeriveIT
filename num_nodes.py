def numNodes(root):
    if not root:
        return 0

    return 1 + numNodes(root.left) + numNodes(root.right)

# Time O(N)
# Space O(N)