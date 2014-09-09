class BinarySearchTree(object):
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, tree):
        current = self
        searching = True
        while searching:
            if tree.data > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = tree
                    searching = False
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = tree
                    searching = False

if __name__ == '__main__':
    tree1 = BinarySearchTree(4)
    tree2 = BinarySearchTree(5)
    tree3 = BinarySearchTree(7)
    tree4 = BinarySearchTree(6)
    tree5 = BinarySearchTree(3)
    tree1.insert(tree2)
    tree1.insert(tree3)
    tree1.insert(tree4)
    tree1.insert(tree5)




