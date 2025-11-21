import tkinter as tk
from tkinter import messagebox

def register():
    name = name_var.get()
    email = email_var.get()
    password = pass_var.get()
    mobile = mobile_var.get()

    if name == "" or email == "" or password == "" or mobile == "":
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", "Registration Successful!")

# Main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("350x400")

# Variables
name_var = tk.StringVar()
email_var = tk.StringVar()
pass_var = tk.StringVar()
mobile_var = tk.StringVar()

# Title Label
tk.Label(root, text="Registration Form", font=("Arial", 16, "bold")).pack(pady=10)

# Name
tk.Label(root, text="Full Name").pack()
tk.Entry(root, textvariable=name_var).pack(pady=5)

# Email
tk.Label(root, text="Email").pack()
tk.Entry(root, textvariable=email_var).pack(pady=5)

# Password
tk.Label(root, text="Password").pack()
tk.Entry(root, textvariable=pass_var, show="*").pack(pady=5)

# Mobile
tk.Label(root, text="Mobile Number").pack()
tk.Entry(root, textvariable=mobile_var).pack(pady=5)

# Submit Button
tk.Button(root, text="Register", command=register, bg="green", fg="white").pack(pady=20)
1
root.mainloop()
