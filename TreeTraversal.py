class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binaryTree:
    def __init__(self):
        self.root = None

# PreOrder traversal
    def PreOrder(self,root):
        if root is None:
            return
        else:
            print(root.data, sep=" ")
            self.PreOrder(root.left)
            self.PreOrder(root.right)
# PostOrder traversal
    def PostOrder(self,root):
        if root is None:
            return
        else:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.data, sep=" ")
# InOrder traversal
    def InOrder(self,root):
        if root is None:
            return
        else:
            self.InOrder(root.left)
            print(root.data, sep=" ")
            self.InOrder(root.right)

tree = binaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("PreOder is: ")
tree.PreOrder(tree.root)
print("PostOrder is:")
tree.PostOrder(tree.root)
print("InOrder is: ")
tree.InOrder(tree.root)
        