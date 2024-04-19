def buildBinarySearchTree(arr):
    def build(i, j):
        if j == i - 1:
            return
        
        mid = ( i + j ) // 2
        node = TreeNode(arr[mid])

        node.left = build(i, mid - 1)
        node.right = build(mid + 1, j)

        return node
    

    return build(0, len(arr)-1)

# Time O(n)
# Space ( log n ) for callstack, but recursively its O(n)
