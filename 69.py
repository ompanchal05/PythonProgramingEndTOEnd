from tkinter import *

# Create window
root = Tk()
root.title("Registration Form")
root.geometry("300x300")

# Labels
Label(root, text="Registration Form", font=("Arial", 14, "bold")).pack(pady=10)
Label(root, text="Name").pack()
name = Entry(root)
name.pack()

Label(root, text="Email").pack()
email = Entry(root)
email.pack()

Label(root, text="Phone").pack()
phone = Entry(root)
phone.pack()

Label(root, text="Gender").pack()
gender = StringVar()
Radiobutton(root, text="Male", variable=gender, value="Male").pack()
Radiobutton(root, text="Female", variable=gender, value="Female").pack()

Label(root, text="").pack()
Button(root, text="Register", bg="green", fg="white").pack()

root.mainloop()