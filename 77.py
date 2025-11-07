#5. Registration Form using Tkinter

import tkinter as tk
from tkinter import messagebox

# Function to display form data
def register():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()
    messagebox.showinfo("Registration Successful", f"Name: {name}\nEmail: {email}\nGender: {gender}")

# Main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x300")

# Labels and Entries
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Gender radio buttons
tk.Label(root, text="Gender:").pack()
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Submit button
tk.Button(root, text="Register", command=register, bg="green", fg="white").pack(pady=10)

root.mainloop()
