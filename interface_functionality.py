import tkinter as tk
import keyboard

def show_popup():
    popup = tk.Toplevel()
    popup.title("Popup Window")

    # Make the popup fullscreen
    popup.attributes("-fullscreen", True)

    # Bring the popup to the front and make it active
    popup.attributes("-topmost", True)
    popup.focus_force()

    label = tk.Label(popup, text="You pressed Ctrl + Shift + L!")
    label.pack(pady=20)

    def close_popup(event=None):
        popup.destroy()

    popup.bind('<Escape>', close_popup)
    popup.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable the close button

    # close_button = tk.Button(popup, text="Close", command=close_popup)
    # close_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Use the keyboard library to add a hotkey for Ctrl + Shift + L
keyboard.add_hotkey('ctrl+shift+l', show_popup)

# Keep the script running
print("Press Ctrl + Shift + L to show the popup. Press Esc to close the popup.")
root.mainloop()
