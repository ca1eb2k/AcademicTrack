# Import all libraries
import tkinter as tk
from tkinter import *
import datetime
from tkinter import Tk, Button, PhotoImage, Label, font

# Function that updates the date by delta (delta is 1 day or change in)
def update_date(delta):
    global current_date  # Get the global variable 'current_date', global is created outside of the function
    save_subject_entries()  # Call the function to save subject entries
    current_date += delta  # Update the current date by adding the delta
    date_label.config(text=current_date.strftime("%Y-%m-%d"))  # Update the date label with .config() which changes strings
    update_subject_entries()  # Update the subject entries with new date

# function to update subject entries based on the current date
def update_subject_entries():
    current_subjects = subjects_data.get(current_date, [""] * 5)  # Get thesubjects for the urrent date or make some empty ones
    for i in range(5):
        subject_entries[i].delete(0, "end")  # Get Rid of the stuff already in the subject entry box
        subject_entries[i].insert(0, current_subjects[i])  # Put in the new subject data

# Function to move to the previous date
def go_back():
    update_date(datetime.timedelta(days=-1))

# Function to move to the next date
def go_forward():
    update_date(datetime.timedelta(days=1))


# Function to save the entered subject entries
def save_subject_entries():
    subjects_data[current_date] = [entry.get() for entry in subject_entries]  # Store subject entries in the dictionary
    with open("subject_data.txt", "a") as file:  # Open the file with "a" to add to without deleting
        file.write(f"{current_date.strftime('%Y-%m-%d')}: {' | '.join(subjects_data[current_date])}\n")  # Write data


# Create the main tkinter window
root = Tk()
root.title("AcademicTracker - Homework Journal")
root.iconbitmap("assets/at_logo.ico")
root.geometry("1000x600")

# Initialize the current date to the current system date and time
current_date = datetime.datetime.now()

# Create and configure the label to display the current date
date_label = Label(root, font=("Helvetica", 14))
date_label.grid(column=0, row=0, columnspan=2, padx=30)
date_label.config(text=current_date.strftime("%Y-%m-%d"))

# Create labels for each subject
L1 = Label(root, text="Subject 1", font=("Helvetica", "12"))
L1.grid(column=0,row=1)
L1 = Label(root, text="Subject 2", font=("Helvetica", "12"))
L1.grid(column=0,row=2)
L1 = Label(root, text="Subject 3", font=("Helvetica", "12"))
L1.grid(column=0,row=3)
L1 = Label(root, text="Subject 4", font=("Helvetica", "12"))
L1.grid(column=0,row=4)
L1 = Label(root, text="Subject 5", font=("Helvetica", "12"))
L1.grid(column=0,row=5)

# Create entry widgets for subject data
L1 = Entry(root, width=150)
L1.grid(column=1,row=1)
L1 = Entry(root, width=150)
L1.grid(column=1,row=2)
L1 = Entry(root, width=150)
L1.grid(column=1,row=3)
L1 = Entry(root, width=150)
L1.grid(column=1,row=4)
L1 = Entry(root, width=150)
L1.grid(column=1,row=5)

# Load left and right arrow images for the buttons that change the days
leftbuttonimg = PhotoImage(file="assets/left_arrow.png")
rightbuttonimg = PhotoImage(file="assets/right_arrow.png")

# Create navigation buttons for moving to previous and next dates
left_button = Button(root, image=leftbuttonimg, command=go_back)
left_button.grid(column=0, row=6, columnspan=2)
right_button = Button(root, image=rightbuttonimg, command=go_forward)
right_button.grid(column=1, row=6, columnspan=2)

# Initialize dictionaries and lists to store subject data and entry widgets
subjects_data = {}  # Dictionary to store subject data for each day
subject_entries = []  # List to store subject entry widgets

# Create entry widgets for subject data and populate existing data if available
for i in range(5):
    entry = Entry(root, width=150)  # Create a new entry widget
    entry.grid(column=1, row=i + 1)  # Position the entry widget
    subject_entries.append(entry)  # Store the entry widget in the list

    # Load existing subject data from the text file if available
    with open("subject_data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(": ")
            if len(parts) == 2:
                date_str, subjects_str = parts
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                subjects = subjects_str.split(" | ")
                subjects_data[date] = subjects

update_subject_entries() # wen opened, update the subject entries

# Create a save button to save the subject entries
save_button = Button(root, text="Save", command=save_subject_entries)
save_button.grid(column=1, row=7, columnspan=2)

root.mainloop()
