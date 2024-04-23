def isBinarySearchTree(root):
    prev = float('-inf')
    BST = True
    def isBST(node):
        nonlocal prev, BST

        if not node or not BST :
            return True
        
        isBST(node.left)

        if not prev < node.val:
            BST = False
        prev = node.val

        isBST(node.right)
        
    isBST(root)
    return BST

    # Time O(N)
    # Space O(N)