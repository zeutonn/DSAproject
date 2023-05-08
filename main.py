import tkinter as tk

# Define a node class for the binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

# Create a function to insert a value into the binary tree
def insert_node(root, value):
    if root is None:
        root = Node(value)
    elif value < root.value:
        root.left_child = insert_node(root.left_child, value)
    else:
        root.right_child = insert_node(root.right_child, value)
    return root
# Delete a node from the binary tree
def delete_node(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = get_min_value_node(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)
    return root

# Get the node with the minimum value in a binary tree
def get_min_value_node(root):
    current = root
    while(current.left is not None):
        current = current.left
    return current

# Create the binary tree with the given values
root = None
root = insert_node(root, 5)
root = insert_node(root, 6)
root = insert_node(root, 7)
root = insert_node(root, 88)
root = insert_node(root, 12)
root = insert_node(root, 45)

# Create a function to display the binary tree in a Tkinter window
def display_tree(root, x, y, canvas, radius=20):
    if root is None:
        return
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill='white', outline='black')
    canvas.create_text(x, y, text=str(root.value), font=("Arial", 14))
    if root.left_child is not None:
        x1, y1 = x-50, y+50
        canvas.create_line(x, y, x1, y1)
        display_tree(root.left_child, x1, y1, canvas, radius)
    if root.right_child is not None:
        x2, y2 = x+50, y+50
        canvas.create_line(x, y, x2, y2)
        display_tree(root.right_child, x2, y2, canvas, radius)

# Create a function to handle the insertion of a node into the binary tree
def insert_node_handler():
    value = entry.get()
    if value:
        value = int(value)
        global root
        root = insert_node(root, value)
        canvas.delete('all')
        display_tree(root, 250, 50, canvas)

def delete_node_handler():
    value = entry.get()
    if value:
        value = int(value)
        global root
        root = delete_node(root, value)
        canvas.delete('all')
        display_tree(root, 250, 50, canvas)
#Inorder Traversal
def inorder_traversal(root, traversal_result):
    if root:
        inorder_traversal(root.left_child, traversal_result)
        traversal_result.append(root.value)
        inorder_traversal(root.right_child, traversal_result)
        


# Create a new Tkinter window
window = tk.Tk()

# Create a canvas to display the binary tree
canvas = tk.Canvas(window, width=500, height=500, bg='white')
canvas.pack()

# Display the binary tree on the canvas
display_tree(root, 250, 50, canvas)

# Create a label and entry widget for inserting a new node
label = tk.Label(window, text="Insert a new node:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button for inserting a new node
button = tk.Button(window, text="Insert", command=insert_node_handler)
button.pack()

# Create a label and deletion widget for deleting a new node
label = tk.Label(window, text="Delete a new node:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button for deleting a new node
button = tk.Button(window, text="Delete", command=delete_node_handler)
button.pack()

# Create labels and buttons for each traversal type
inorder_label = tk.Label(window, text="Inorder Traversal:")
inorder_label.pack(side="left")
inorder_result = tk.Label(window, text="")
inorder_result.pack(side="left")
inorder_button = tk.Button(window, text="Traverse", command=lambda: inorder_click(root, inorder_result))
inorder_button.pack(side="left")

preorder_label = tk.Label(window, text="Preorder Traversal:")
preorder_label.pack(side="left")
preorder_result = tk.Label(window, text="")
preorder_result.pack(side="left")
preorder_button = tk.Button(window, text="Traverse", command=lambda: preorder_click(root, preorder_result))
preorder_button.pack(side="left")

postorder_label = tk.Label(window, text="Postorder Traversal:")
postorder_label.pack(side="left")
postorder_result = tk.Label(window, text="")
postorder_result.pack(side="left")
postorder_button = tk.Button(window, text="Traverse", command=lambda: postorder_click(root, postorder_result))
postorder_button.pack(side="left")

# Define the traversal functions
def inorder_click(node, result_label):
    traversal_result = []
    inorder_traversal(node, traversal_result)
    result_label.config(text=str(traversal_result))

def preorder_click(node, result_label):
    traversal_result = []
    preorder_traversal(node, traversal_result)
    result_label.config(text=str(traversal_result))

def postorder_click(node, result_label):
    traversal_result = []
    postorder_traversal(node, traversal_result)
    result_label.config(text=str(traversal_result))

# Run the window's main event loop
window.mainloop()
