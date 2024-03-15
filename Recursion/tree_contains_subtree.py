def sameTree(root, subRoot):
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        left = sameTree(root.left, subRoot.left)
        right = sameTree(root.right, subRoot.right)

        return root.val == subRoot.val and left and right

def containsSubtree(root, subRoot):
    if not root:
        return False

    return sameTree(root, subRoot) or containsSubtree(root.left, subRoot) or containsSubtree(root.right, subRoot)

    #Time O(m * n)
    #Space O(m + n)