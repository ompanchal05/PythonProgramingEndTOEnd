# WAP FOR THE  Basic Tkinter Example 

# 🪟 Basic Tkinter Example
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("My First Tkinter App")

# Set window size (Width x Height)
root.geometry("400x250")

# Add a label widget
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16), fg="blue")
label.pack(pady=20)

# Add an entry (text box)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Function to display the entered text
def show_message():
    user_input = entry.get()
    label.config(text=f"Welcome, {user_input}!")

# Add a button
button = tk.Button(root, text="Click Me", command=show_message, bg="lightgreen", font=("Arial", 12))
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
