import tkinter as tk
import subprocess
from tkinter import Tk, messagebox


def center_window(window):
    """
    Center the given window on the screen.

    Parameters:
    - window: The Tkinter window to be centered.
    """
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


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



def open_program(file_path):
    subprocess.call(['python', file_path])


# Create the main Tkinter window
root = Tk()

# Set the window title, icon, and size
root.title("AcademicTracker - Login/Sign Up")
root.geometry("1000x600")

# Create a centered heading label using Helvetica font
heading_label = tk.Label(root, text="AcademicTracker",
                         font=("Helvetica", 40, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

# Create labels and entry boxes for username, email, and password
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

# Change grid columns to center widgets
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
        messagebox.showerror("Invalid Password",
                             "Password needs 1 capital letter,",
                             "8+ chars, and 1 number.")
        return None
    else:
        return username, email, password


def write_to_file():
    login_info = get_userdata()
    if login_info is None:
        return
    with open("logininfo.txt", "r") as file:
        input_string = file.read()

    # Process data from the file
    parts = input_string.split("\n")
    processed_data = []

    for part in parts:
        if part:
            part = part.replace("(", "").replace(")", "")
            part = part.replace("'", "").split(', ')
            processed_data.append(tuple(part))

    # Check if the entered data matches any existing data
    for data in processed_data:
        if data == login_info:
            return True

    # Add the new login info to the file on a new line
    with open("logininfo.txt", "a") as file:
        file.write(str(login_info) + "\n")


def read_and_verify():
    login_info = get_userdata()
    if login_info is None:
        return
    with open("logininfo.txt", "r") as file:
        input_string = file.read()

    # Process data from the file
    parts = input_string.split("\n")
    processed_data = []

    for part in parts:
        if part:
            part = part.replace("(", "").replace(")", "")
            part = part.replace("'", "").split(', ')
            processed_data.append(tuple(part))

    # Check if the entered data matches any
    # existing data and open the program if found
    for data in processed_data:
        if data == login_info:
            print("found")  # Print a message for testing, can be removed
            open_program("menu.py")
            return True


sign_up_button = tk.Button(root,
                           text="Sign Up", font=40, command=write_to_file)
sign_up_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

log_in_button = tk.Button(root, text="Log In",
                          font=40, command=read_and_verify)
log_in_button.grid(row=4, column=1)

center_window(root)
root.mainloop()
