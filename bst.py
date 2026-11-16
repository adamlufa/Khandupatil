'''
ummehabiba shaikh SE-B2-30

Problem statement: beginning with an empty binary search tree by inserting the 
values in the order given after constructing a binary to tree
'''
# Group D Assignment 3 - BST Operations


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            # Node with no child or one child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root

    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)


# Main program
bst = BST()
root = None

# Inserting nodes
key_str = input("Enter keys: ").split()
keys = [int(key) for key in key_str]

for key in keys:
    root = bst.insert(root, key)

print("In-order Traversal of the BST:")
bst.inorder(root)
print()

print("Preorder Traversal of the BST:")
bst.preorder(root)
print()

# Search
key_to_search = int(input("Enter key to search: "))

result = bst.search(root, key_to_search)

if result:
    print(f"Key {key_to_search} found in BST.")
else:
    print(f"Key {key_to_search} not found in BST.")

# Delete a node
key_to_delete = int(input("Key to delete: "))

root = bst.delete(root, key_to_delete)

print(f"In-order after deleting {key_to_delete}:")
bst.inorder(root)
print()


'''
gescoe@gescoe-OptiPlex-3020:~$ python3 bst_operations.py
Enter keys: 5 10 2 15
In-order Traversal of the BST:
2 5 10 15 
Preorder Traversal of the BST:
5 2 10 15 
Enter key to search: 10
Key 10 found in BST.
Key to delete: 10
In-order after deleting 10:
2 5 15 
'''


