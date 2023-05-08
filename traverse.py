from main import Node

def inorder_traversal(root, traversal_result):
    if root:
        inorder_traversal(root.left_child, traversal_result)
        traversal_result.append(root.value)
        inorder_traversal(root.right_child, traversal_result)

def preorder_traversal(root, traversal_result):
    if root:
        traversal_result.append(root.value)
        preorder_traversal(root.left_child, traversal_result)
        preorder_traversal(root.right_child, traversal_result)

def postorder_traversal(root, traversal_result):
    if root:
        postorder_traversal(root.left_child, traversal_result)
        postorder_traversal(root.right_child, traversal_result)
        traversal_result.append(root.value)
