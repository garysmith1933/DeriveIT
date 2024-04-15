a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
f = TreeNode("F")
g = TreeNode("G")
a.left, a.right = b, c
b.left, b.right = d, e
e.left, e.right = f, g

# # preorder
# def visitAll(node): node, left, right
#     if not node: 
#         return
#     print(node.val)
#     visitAll(node.left)
#     visitAll(node.right)

# #postorder - left, right, node
# def visitAll(node):
#     if not node: 
#         return
    
#     visitAll(node.left)
#     visitAll(node.right)
#     print(node.val)

#inorder - left, node, right
def visitAll(node):
    if not node: 
        return
    
    visitAll(node.left)
    print(node.val)
    visitAll(node.right)

# print preorder traversal
def test():
    visitAll(a)