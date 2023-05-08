import tkinter  as Tk
from tree import BinarySearchTree
import random

# Create a window
window = Tk()
window.title("Binary Search Tree")

# Create a canvas to draw the tree on
canvas_width = 8000
canvas_height = 6000
canvas = Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()
  # Add scrollbar to canvas
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a binary search tree
bst = BinarySearchTree(canvas, canvas_width // 2, 50)

# Generate 10,000 random numbers and insert them into the tree
for i in range(10):
    bst.insert(random.randint(1, 10))

# Start the main loop
window.mainloop()
