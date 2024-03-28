def fileDestroyer(root):
    res = []

    def delete(node):
        if not node:
            return 
        
        print(node.val)
        
        delete(node.left)
        delete(node.right)
        res.append(node.val)
    
    delete(root)
    return res
    # Time O(N)
    #Space O(N)