class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def _height(self, node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _get_balance(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_left(self, y):
        x = y.right
        y.right = x.left
        x.left = y
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        self._update_height(x)
        self._update_height(y)
        return y

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        self._update_height(node)
        balance = self._get_balance(node)
        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def inorder_traversal(self, node):
        result = []
        if node:
            result += self.inorder_traversal(node.left)
            result.append(node.key)
            result += self.inorder_traversal(node.right)
        return result

# Create an empty AVL tree
avl_tree = AVLTree()
keys = []

# Get user input for inserting elements
while True:
    user_input = input("Enter an element to insert (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        key = int(user_input)
        avl_tree.insert(key)
        keys.append(key)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Display the inorder traversal of the AVL tree
print("Inorder traversal of the AVL tree:")
inorder_result = avl_tree.inorder_traversal(avl_tree.root)
print(inorder_result)
