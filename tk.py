import tkinter as tk
from src.auth import login_user  # tumhara backend logic

def login():
    username = entry_username.get()
    password = entry_password.get()
    if login_user(username, password):
        label_result.config(text="Login Successful")
    else:
        label_result.config(text="Login Failed")

root = tk.Tk()
root.title("Login Page")

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack()
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
