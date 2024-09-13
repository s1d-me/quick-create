import tkinter as tk
from tkinter import simpledialog
import pyperclip
import requests
from pynput import keyboard
import pystray
from PIL import Image, ImageDraw
import threading

# Configuration
API_TOKEN = 'question123'
API_URL = 'https://s1d.me/api/shorten'
KEYBIND = '<ctrl>+<shift>+l'  # Change this to your desired keybind

def shorten_url(url):
    headers = {
        'Authorization': API_TOKEN,
        'Content-Type': 'application/json'
    }
    data = {
        "url": url,
        "length": 6,
        "allow_numbers": True,
        "allow_uppercase": True,
        "allow_lowercase": True,
        "expiry_time": "2024-09-12 23:59:59"
    }
    response = requests.post(API_URL, json=data, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        return response.json().get('short_code')
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def on_activate():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.attributes("-topmost", True)  # Make the dialog appear on top
    url = simpledialog.askstring("Input", "Enter the URL to shorten:", parent=root)
    if url:
        short_code = shorten_url(url)
        if short_code:
            shortened_url = f"https://s1d.me/{short_code}"
            pyperclip.copy(shortened_url)
            print(f"Shortened URL: {shortened_url} (copied to clipboard)")
        else:
            print("Failed to shorten the URL.")
    root.destroy()

def on_press(key):
    if key == keyboard.Key.ctrl_l and keyboard.Controller().pressed(keyboard.Key.shift):
        on_activate()

def create_image():
    # Generate an image for the system tray icon
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2), fill='black')
    dc.rectangle((0, height // 2, width // 2, height), fill='black')
    return image

def on_clicked(icon, item):
    if str(item) == "Exit":
        icon.stop()
        listener.stop()

listener = keyboard.Listener(on_press=on_press)

icon = pystray.Icon("URL Shortener")
icon.icon = create_image()
icon.menu = pystray.Menu(
    pystray.MenuItem("Exit", on_clicked)
)

# Start the listener in a separate thread
listener_thread = threading.Thread(target=listener.start)
listener_thread.start()

# Run the system tray icon
icon.run()
