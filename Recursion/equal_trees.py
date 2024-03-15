def treesEqual(p, q):
    if not p and not q:
        return True
    
    if not p or not q or p.val != q.val:
        return False
    
    return treesEqual(p.left, q.left) and treesEqual(p.right, q.right)

    #Time O(min(m,n))
    #Space O(min(m, n))