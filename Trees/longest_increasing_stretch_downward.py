def longestIncrStretch(root):
    longest = float('-inf')

    def stretch(node, prevVal, prevLen):
        if node is None:
            return 

        curLen = 1

        if node.val > prevVal:
            curLen = curLen + prevLen
        
        nonlocal longest
        longest = max(curLen, longest)
        
        left = stretch(node.left, node.val, curLen)
        right = stretch(node.right, node.val, curLen)
    

    stretch(root, float('-inf'), 0)
    return longest

#Time O(N)
#Space O(N)