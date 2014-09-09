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


def in_order(tree):
    if tree is None:
        return
    else:
        in_order(tree.left)
        print tree.data
        in_order(tree.right)


def insert_sorted_array(input_array):
    mid_point = len(input_array) // 2
    tree = BinarySearchTree(input_array[mid_point])
    insert_right = mid_point + 1
    insert_left = mid_point -1
    while insert_right < len(input_array):
        tree.insert(BinarySearchTree(input_array[insert_right]))
        insert_right += 1
    while insert_left >= 0:
        tree.insert(BinarySearchTree(input_array[insert_left]))
        insert_left -= 1
    return tree




# book solution, way cooler than mine
# makes binary search tree from binary tree using recursion

# class BinaryTree:
#     def __init__(self, content, left = None, right = None):
#         self.content = content
#         self.left = left
#         self.right = right

#     def __str__(self):
#         return "( " + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) + "))"

# #Given a sorted (increasing order) array with unique integer elements, write an
# #algorithm to create a binary search tree with minimal height.


# def int_array_to_binary_search_tree(intarray):
#     #use the middle of the array to divide it. this ensures minimal height.
#     if len(intarray) == 0:
#         return None
#     if len(intarray) == 1:
#         return BinaryTree(intarray[0])
#     cut = len(intarray) / 2
#     return BinaryTree( intarray[cut], \
#         int_array_to_binary_search_tree(intarray[0:cut]),
#         int_array_to_binary_search_tree(intarray[cut+1:]))