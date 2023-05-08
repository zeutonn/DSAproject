import tkinter as tk
import random

class TreeNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return

        curr = self.root
        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return
                curr = curr.right

    def traverse_inorder(self, node):
        if node:
            self.traverse_inorder(node.left)
            print(node.val, end=" ")
            self.traverse_inorder(node.right)

def add_node(canvas, x, y, text):
    r = 20
    canvas.create_oval(x-r, y-r, x+r, y+r, fill='white')
    canvas.create_text(x, y, text=text)

def draw_tree(canvas, root, x, y, x_diff, y_diff):
    if root:
        add_node(canvas, x, y, root.val)
        if root.left:
            x_new = x - x_diff
            y_new = y + y_diff
            canvas.create_line(x, y, x_new, y_new)
            draw_tree(canvas, root.left, x_new, y_new, x_diff/2, y_diff)
        if root.right:
            x_new = x + x_diff
            y_new = y + y_diff
            canvas.create_line(x, y, x_new, y_new)
            draw_tree(canvas, root.right, x_new, y_new, x_diff/2, y_diff)

if __name__ == '__main__':
    bst = BST()
    for i in range(100):
        bst.insert(random.randint(1, 100))

    root = bst.root

    master = tk.Tk()
    master.title("Binary Search Tree")

    canvas_width = 1366
    canvas_height = 768
    canvas = tk.Canvas(master, width=canvas_width, height=canvas_height)
    canvas.pack()

    x = canvas_width // 2
    y = 50
    x_diff = 500
    y_diff = 100

    draw_tree(canvas, root, x, y, x_diff, y_diff)

    master.mainloop()
