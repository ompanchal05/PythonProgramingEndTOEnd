#wap to understand Tkinter. 
# 📘 Understanding Tkinter – Basic Example

import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Understanding Tkinter")
root.geometry("400x250")  # Set window size

# Create a label widget
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

# Define button click event
def greet_user():
    name = entry.get()
    if name:
        messagebox.showinfo("Greeting", f"Hello, {name}! 👋")
    else:
        messagebox.showwarning("Input Error", "Please enter your name!")

# Create a button widget
button = tk.Button(root, text="Greet Me", command=greet_user, font=("Arial", 12), bg="lightblue")
button.pack(pady=15)

# Add an exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12), bg="tomato")
exit_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
