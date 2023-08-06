import tkinter as tk
from tkinter import *

root=Tk()

width = 1000
height = 600
root.geometry(f"{width}x{height}")

# Create a centered heading label
heading_label = tk.Label(root, text="AcademicTracker", font=("Helvetica", 40, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

# Create labels and entry boxes
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


# Configure grid columns to center widgets
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


# function that when activated saves all entered data from the boxes into variables, and gives the 3 variables listed
def get_userdata():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    print(username, email, password) # delete in final version
    return username, email, password # function gives 3 variables listed


# function to check if the entered info is already in text database, and if not, write login info to the file
def write_to_file():
    login_info = get_userdata() # variable login_info is now populated with userdata (username, email, password)
    with open("output.txt", "r") as file: # using python feature to open the output file
        input_string = file.read() # input_string variable is filled with all the data from the file

    parts = input_string.split("\n") # splitting the complete file from one string into elements based on every newline
    processed_data = []  # initialize an empty list to store processed data (tuples)

    for part in parts:
        if part: # checking if the part is not an empty string / or a line that is not empty
            part = part.replace("(", "").replace(")", "").replace("'", "").split(', ')
            processed_data.append(tuple(part)) # processing each part and converting it into a tuple, then adding it to processed_data list

    for data in processed_data: # iterating through each tuple in processed_data list
        if data == login_info: # checking if the current tuple matches the login information givem by the user
            print("Error") # if there is a match, print an error message, delete in final version
            return True # and return True if a match is found

    login_info = get_userdata() # variable login_info is now populated with userdata (username, email, password)
    with open("output.txt", "a") as file: # opening text file with "a" to write to the file without deleting anything in it
        file.write(str(login_info) + "\n") # write to the file the login info given, and add a newline.


def read_and_verify():
    login_info = get_userdata()
    with open("output.txt", "r") as file:
        input_string = file.read()

    parts = input_string.split("\n")
    processed_data = []

    for part in parts:
        if part:
            part = part.replace("(", "").replace(")", "").replace("'", "").split(', ')
            processed_data.append(tuple(part))

    for data in processed_data:
        if data == login_info:
            print("found")
            return True


SIGN_UP_BUTTON = tk.Button(root, text="Sign Up", font=40, command=write_to_file)
SIGN_UP_BUTTON.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

LOG_IN_BUTTON = Button(root, text="Log In", font=40, command=read_and_verify)
LOG_IN_BUTTON.grid(row=4, column=1)


root.mainloop()






