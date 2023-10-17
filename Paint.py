from tkinter import *
from tkinter.colorchooser import askcolor

# Define the drawing class
class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.configure(background="white")

        # Create a canvas widget for drawing
        self.canvas = Canvas(root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # Initialize variables
        self.pointer = "black"
        self.erase = "white"
        self.pen_size = 2
        self.eraser_size = 10
        self.drawing_mode = True  # True for drawing, False for erasing

        # Create buttons
        self.mode_button = Button(root, text="Erase", command=self.toggle_mode)
        self.mode_button.pack()
        
        self.color_button = Button(root, text="Pick Color", command=self.pick_color)
        self.color_button.pack()
        
        self.increase_button = Button(root, text="Increase Size", command=self.increase_size)
        self.increase_button.pack()
        
        self.decrease_button = Button(root, text="Decrease Size", command=self.decrease_size)
        self.decrease_button.pack()

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

    def toggle_mode(self):
        if self.drawing_mode:
            self.drawing_mode = False
            self.mode_button.config(text="Draw")
        else:
            self.drawing_mode = True
            self.mode_button.config(text="Erase")

    def pick_color(self):
        color = askcolor()[1]
        if self.drawing_mode:
            self.pointer = color
        else:
            self.erase = color

    def increase_size(self):
        if self.drawing_mode:
            self.pen_size += 1
        else:
            self.eraser_size += 1

    def decrease_size(self):
        if self.drawing_mode:
            self.pen_size = max(1, self.pen_size - 1)
        else:
            self.eraser_size = max(1, self.eraser_size - 1)

    def start_drawing(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        x, y = event.x, event.y
        if self.drawing_mode:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.pointer, width=self.pen_size)
        else:
            self.canvas.create_oval(x - self.eraser_size, y - self.eraser_size, x + self.eraser_size, y + self.eraser_size, fill=self.erase, outline=self.erase)
        self.last_x = x
        self.last_y = y

# Create a Tkinter window
root = Tk()

# Initialize the drawing application
drawing_app = DrawingApp(root)

# Start the main event loop
root.mainloop()