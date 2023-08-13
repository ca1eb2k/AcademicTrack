"""
This file is for the login page of the AcademicTracker application.

It provides a graphical user interface (GUI) for users to log in or sign up.
The user can enter their username, email, and password.
The password is validated to ensure it meets specific criteria:
At least 8 characters, containing at least one uppercase
letter, and at least one digit.

The user can either sign up or log in. If signing up, the entered information
is validated and stored in a file named "logininfo.txt".
If logging in, the entered information is compared with the stored
data to determine if the user's credentials are valid. If so, it opens another
program named "menu.py" using the `open_program` function.

The GUI is built using the tkinter library.
The layout includes labels and entry boxes for the
username, email, and password.
The sign-up and log-in buttons trigger functions to
handle user interaction and data processing.

Functions:
- is_valid_password(password): Validates whether a password
meets the required criteria.
- open_program(file_path): Opens another Python
program using the subprocess module.
- get_userdata(): Retrieves and validates user data from the entry boxes.
- write_to_file(): Checks user data against existing
data and writes to the "logininfo.txt" file.
- read_and_verify(): Reads and verifies user data
from the file and opens the "menu.py" program if data is found.
"""

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
    """
    Check if the given password meets the required criteria.

    Parameters:
    password (str): The password to be validated.

    Returns:
    bool: True if the password is valid, False otherwise.
    """
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


# Function to open another Python program using subprocess
def open_program(file_path):
    """
    Open another Python program using subprocess.

    Parameters:
    file_path (str): Path to the Python program file.

    Returns:
    None
    """
    subprocess.call(['python', file_path])


# Create the main Tkinter window
root = Tk()

# Set the window title, icon, and size
root.title("AcademicTracker - Login/Sign Up")
root.iconbitmap("assets/at_logo.ico")
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
    """
    Retrieve user data from the entry boxes and validate the password.

    Returns:
    tuple: A tuple containing the username,
    email, and password entered by the user.
    If any entry box is empty or the password is invalid, returns None.
    """
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not (username and email and password):
        messagebox.showerror(title="Invalid Entry",
                             message="You haven't filled out all three boxes!")
        return None
    elif not is_valid_password(password):
        messagebox.showerror("Invalid Password",
                             "Password needs 1 capital letter," +
                             "8+ chars, and 1 number.")
        return None
    else:
        return username, email, password


def write_to_file():
    """Write data to file.

    Check if entered user data is in the database
    and write to the file if not.
    """
    login_info = get_userdata()
    if login_info is None:
        return
    with open("db/logininfo.txt", "r") as file:
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
    with open("db/logininfo.txt", "a") as file:
        file.write(str(login_info) + "\n")
        messagebox.showinfo("Success", "Sign Up Successful!")


def read_and_verify():
    """Read data from the file.

    Read and verify user data from the file,
    then open the program if data is found.

    """
    login_info = get_userdata()
    if login_info is None:
        return
    with open("db/logininfo.txt", "r") as file:
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

# Used buttons and labels
sign_up_button = tk.Button(root,
                           text="Sign Up", font=40, command=write_to_file)
sign_up_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

log_in_button = tk.Button(root, text="Log In",
                          font=40, command=read_and_verify)
log_in_button.grid(row=4, column=1)

center_window(root)

# Start the main event loop of the Tkinter application
root.mainloop()
