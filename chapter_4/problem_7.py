
class BinaryTree(object):
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.depth = 0


def in_order(tree):
    if tree is None:
        return
    else:
        for n in in_order(tree.left):
            yield n
        yield tree.data
        for n in in_order(tree.right):
            yield n


def find_acenstor(tree, data1, data2):
    right_data = [n for n in in_order(tree.right)]
    left_data = [n for n in in_order(tree.left)]
    if data1 in right_data and data2 in right_data:
        return find_acenstor(tree.right, data1, data2)
    elif data1 in left_data and data2 in left_data:
        return find_acenstor(tree.left, data1, data2)
    else:
        return tree


if __name__ == "__main__":
    tree1 = BinaryTree(1)
    tree2 = BinaryTree(3)
    tree3 = BinaryTree(4)
    tree4 = BinaryTree(7)
    tree5 = BinaryTree(9)
    tree6 = BinaryTree(10)
    tree7 = BinaryTree(11)
    tree4.right = tree7
    tree3.right = tree4
    tree3.left = tree5
    tree1.right = tree3
    tree1.left = tree2
    tree2.left = tree6
    ancestor = find_acenstor(tree1, 9, 7)
    print ancestor.data
