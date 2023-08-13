import tkinter as tk
from tkinter import Tk, messagebox

def is_valid_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True

    return has_upper and has_digit

root = Tk()

root.title("AcademicTracker - Login/Sign Up")

heading_label = tk.Label(root, text="AcademicTracker",
                         font=("Helvetica", 40, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

username_label = tk.Label(root,
                          text="Username", font=("Helvetica", 15, "italic"))
username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email", font=("Helvetica", 15, "italic"))
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(root,
                          text="Password", font=("Helvetica", 15, "italic"))
password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


def get_userdata():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not (username and email and password):
        messagebox.showerror(title="Invalid Entry",
                             message="You haven't filled out all three boxes!")
        return None
    elif not is_valid_password(password):
        messagebox.showerror("Invalid Password", "Password needs 1 capital letter,","8+ chars, and 1 number.")
        return None
    else:
        return username, email, password


def write_to_file():
    login_info = get_userdata()
    if login_info is None:
        return
    with open("output.txt", "r") as file:
        input_string = file.read()

    parts = input_string.split("\n")
    processed_data = []

    for part in parts:
        if part:
            part = part.replace("(", "").replace(")", "")
            part = part.replace("'", "").split(', ')
            processed_data.append(tuple(part))

    for data in processed_data:
        if data == login_info:
            return True

    with open("output.txt", "a") as file:
        file.write(str(login_info) + "\n")


def read_and_verify():
    login_info = get_userdata()
    if login_info is None:
        return
    with open("output.txt", "r") as file:
        input_string = file.read()

    parts = input_string.split("\n")
    processed_data = []

    for part in parts:
        if part:
            part = part.replace("(", "").replace(")", "")
            part = part.replace("'", "").split(', ')
            processed_data.append(tuple(part))

    for data in processed_data:
        if data == login_info:
            print("found")
            return True


sign_up_button = tk.Button(root, text="Sign Up", font=40, command=write_to_file)
sign_up_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

log_in_button = tk.Button(root, text="Log In", font=40, command=read_and_verify)
log_in_button.grid(row=4, column=1)

root.mainloop()