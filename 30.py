import tkinter as tk

# Function to display name
def show_name():
    name = entry.get()  # get text from entry field
    label_result.config(text="Hello, " + name)

# Create main window
root = tk.Tk()
root.title("Simple GUI Program")
root.geometry("300x200")

# Label
label1 = tk.Label(root, text="Enter Your Name:")
label1.pack(pady=5)

# Text Field (Entry)
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Submit", command=show_name)
button.pack(pady=5)

# Label to show result
label_result = tk.Label(root, text="", fg="blue", font=("Arial", 12))
label_result.pack(pady=10)

# Run the GUI loop
root.mainloop()