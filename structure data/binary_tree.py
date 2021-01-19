class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:

    def __init__(self):
        self.root = None


    def insert_node(self,root,element):
        if self.root is None:
            self.root = Node(element)
        else:

            if root is None:
                root = Node(element)
            elif root.data <= element:
                root.right = self.insert_node(root.right,element)
            elif root.data > element:
                root.left = self.insert_node(root.left,element)


        return root

    def PreOrder(self,root):
        if root is not None:
            print(root.data)
            if root.left is not None:
                self.PreOrder(root.left)
            if root.right is not None:
                self.PreOrder(root.right)



a = BinaryTree()
a.insert_node(a.root,3)
a.insert_node(a.root,4)
a.insert_node(a.root,34)
a.insert_node(a.root,45)
a.insert_node(a.root,46)
a.insert_node(a.root,2)
a.insert_node(a.root,48)
a.PreOrder(a.root)