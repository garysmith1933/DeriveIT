def lowestCommonAncestorValue(root, p, q):
    lca = 0

    def findNodes(node):
        if not node:
            return False
        
        leftHas = findNodes(node.left)
        rightHas = findNodes(node.right)
        nodeEquals = (node.val == p or node.val == q)

        if nodeEquals or (leftHas and rightHas):
            nonlocal lca
            lca = node.val
        
        return nodeEquals or leftHas or rightHas
    
    findNodes(root)
    return lca

    #Time O(N)
    #Space O(N)