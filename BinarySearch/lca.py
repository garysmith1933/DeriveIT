def LCA(root, p, q):
    lca = root

    def findLCA(node):
        if not node:
            return

        if p <= node.val and q >= node.val or p >= node.val and q <= node.val:
            nonlocal lca
            lca = node.val
        
        if p < node.val and q < node.val:
            return findLCA(node.left)
        
        if p > node.val and q > node.val:
            return findLCA(node.right)
    
    findLCA(root)
    return lca

#Time O(N)
#Space O(N)