# Import necessary libraries
import tkinter as tk
from tkinter import *
import subprocess
from tkinter import ttk
from tkinter import messagebox

# Function to open another pyython program using subprocess
def open_program(file_path):
    subprocess.call(['python', file_path])

# Create the main Tkinter window
root = Tk()

# Set the window title, icon, and size 
root.title("AcademicTracker - Login/Sign Up")
root.iconbitmap("assets/at_logo.ico")
root.geometry("1000x600")

# Create a centered heading label using helvetica font
heading_label = tk.Label(root, text="AcademicTracker", font=("Helvetica", 40, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

# Create labels and entry boxes for username, email, and password
username_label = tk.Label(root, text="Username", font=("Helvetica", 15,"italic"))
username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email", font=("Helvetica", 15,"italic"))
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Password", font=("Helvetica", 15,"italic"))
password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1, padx=10, pady=5)

# change grid columns to center widgets
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Function to get the entered user data from the entry boxes
def get_userdata():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if all entryboxes have stuff in them
    if not (username and email and password):
        messagebox.showerror(title="Invalid Entry", message="You have not filled out all three boxes!")
        return None # if error have none
    else:
        return username, email, password

# Function to check if entered info is in the database and write to the file if not
def write_to_file():
    login_info = get_userdata()
    if login_info is None:
        return  # if there was an error, dont continue 
    with open("timetableinfo.txt", "r") as file:
        input_string = file.read()

    # Gather tje data from the file
    parts = input_string.split("\n")
    processed_data = []

    for part in parts:
        if part:
            part = part.replace("(", "").replace(")", "").replace("'", "").split(', ')
            processed_data.append(tuple(part))

    # Check if the entered data matches any existing data
    for data in processed_data:
        if data == login_info:
            print("Error")  # Print an error message, delete in the final version
            return True

    # Add the new login info to the file, in a newline 
    with open("timetableinfo.txt", "a") as file:
        file.write(str(login_info) + "\n")

# Function that reads and verifys user data from the file
def read_and_verify():
    login_info = get_userdata()
    if login_info is None:
        return  # if an error dont continue
    with open("timetableinfo.txt", "r") as file:
        input_string = file.read()

    # Gather data from the file
    parts = input_string.split("\n")
    processed_data = []

    for part in parts:
        if part:
            part = part.replace("(", "").replace(")", "").replace("'", "").split(', ')
            processed_data.append(tuple(part))

    # Check if the entered data matches any existing data and open the program if found
    for data in processed_data:
        if data == login_info:
            print("found")  # Print a message for testing, can be removed
            open_program("menu.py")
            return True

# Create buttons for signing up and logging in, with corresponding functions
SIGN_UP_BUTTON = tk.Button(root, text="Sign Up", font=40, command=write_to_file)
SIGN_UP_BUTTON.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

LOG_IN_BUTTON = Button(root, text="Log In", font=40, command=read_and_verify)
LOG_IN_BUTTON.grid(row=4, column=1)

# Start the main event loop of the Tkinter application
root.mainloop()
