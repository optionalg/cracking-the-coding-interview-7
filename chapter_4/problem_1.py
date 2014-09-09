
class BinaryTree(object):
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.depth = 0


def pre_order(binary_tree):
    if binary_tree is None:
        return
    else:
        print binary_tree.data
        pre_order(binary_tree.left)
        pre_order(binary_tree.right)


if __name__ == '__main__':
    tree1 = BinaryTree(1)
    tree2 = BinaryTree(2)
    tree3 = BinaryTree(3)
    tree4 = BinaryTree(4)
    tree1.right = tree3
    tree1.left = tree2
    tree2.right = tree4
    print pre_order(tree1)
