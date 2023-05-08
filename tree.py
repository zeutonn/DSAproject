class BinarySearchTree:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.value = None

    def insert(self, value):
        if self.value is None:
            # If the node is empty, create a new node with the given value
            self.value = value
            self.canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="white", outline="black")
            self.canvas.create_text(self.x, self.y, text=str(value))
        elif value < self.value:
            # If the value is less than the node's value, insert it into the left subtree
            if self.left is None:
                # If the left subtree is empty, create a new subtree with the given value
                self.left = BinarySearchTree(self.canvas, self.x - 100, self.y + 50)
            self.left.insert(value)
        else:
            # If the value is greater than or equal to the node's value, insert it into the right subtree
            if self.right is None:
                # If the right subtree is empty, create a new subtree with the given value
                self.right = BinarySearchTree(self.canvas, self.x + 100, self.y + 50)
            self.right.insert(value)
