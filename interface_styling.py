import tkinter as tk
from tkinter import Toplevel

# Create the main window
root = tk.Tk()

# Make the window transparent
root.overrideredirect(True)  # Remove window decorations (like title bar)
root.wm_attributes("-transparentcolor", root["bg"])  # Set transparency

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the size of the black rectangle
h = int(0.4 * screen_width)  # 40% of screen width
q = int(0.1 * screen_height)  # 10% of screen height

# Center the window
x_position = (screen_width - h) // 2
y_position = (screen_height - q) // 2

# Set the geometry of the window to the size of the black rectangle
root.geometry(f"{h}x{q}+{x_position}+{y_position}")

# Create a label with a black background to act as the rectangle
label = tk.Label(root, bg="white")
label.pack(fill="both", expand=True)

# Make sure the window stays on top
root.wm_attributes("-topmost", True)

# Run the window
root.mainloop()
