def maximumPathSum(root):
    res = float('-inf')

    def sum_path(node):
        if not node:
            return 0

        left = sum_path(node.left)
        right = sum_path(node.right)

        max_path = node.val + max(left, right, left + right, 0)

        nonlocal res
        res = max(res, max_path)

        return node.val + max(left, right, 0)
        
    sum_path(root)
    return res