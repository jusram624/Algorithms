class TreeNode:
    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
class Traversal:
    def inOrder(self, root): 
        if root == None:
            return
        self.inOrder(root.left)
        print(root.data, end = ' ')
        self.inOrder(root.right)

    def preOrder(self, root):
        if root == None:
            return
        print(root.data, end = ' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def postOrder(self, root):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end = ' ')


tree = TreeNode(2, TreeNode(7, TreeNode(2), TreeNode(6, TreeNode(5), TreeNode(11))), TreeNode(5,None, TreeNode(9, TreeNode(4))) )
traversal = Traversal()
traversal.inOrder(tree)
print()
traversal.preOrder(tree)
print()
traversal.postOrder(tree)