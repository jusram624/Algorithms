class TreeNode:
    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BFS:
    def bfs(self, root):
        q = [root]
        while q: 
            for i in range(len(q)):
                curr = q.pop(0)
                print(curr.data, end = ' ')
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        print()

tree = TreeNode(2, TreeNode(7, TreeNode(2), TreeNode(6, TreeNode(5), TreeNode(11))), TreeNode(5,None, TreeNode(9, TreeNode(4))) )
traversal = BFS()
traversal.bfs(tree)