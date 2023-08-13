"""This script implements a Homework Journal in the app.

The script provides an interface for users to record
homework information for different subjects.
Users can navigate between different dates and input
homework data for up to 5 subjects.
The entered data is saved to a file named "subject_data.txt"
with the corresponding date.

Functions:
- update_date(delta): Updates the current date and subject
entries based on the given delta (change in days).
- update_subject_entries(): Updates subject entries based
on the current date.
- go_back(): Moves to the previous date.
- go_forward(): Moves to the next date.
- save_subject_entries(): Saves entered subject entries
to the dictionary and file.

GUI Components:
- Main Tkinter window (root): The main window of the Homework
Journal.
- Labels for date and subjects (date_label, L1).
- Entry boxes for subjects (L1).
- Buttons for navigation (left_button, right_button).
- Button to save subject entries (save_button).

Layout:
- Labels, entry boxes, and buttons are positioned
in a grid layout using the grid method.

Execution:
- The main event loop of the Tkinter application is
started using root.mainloop().
"""

from tkinter import *
import datetime
from tkinter import Tk, Button, PhotoImage, Label, Entry

# Function to center the window on the screen.
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

def update_date(delta):
    """Update time.

    Update the date by adding a delta (change in days)
    and update subject entries accordingly.

    Parameters:
    delta (datetime.timedelta): The change in days to
    update the current date.

    Returns:
    None
    """
    global current_date
    save_subject_entries()
    current_date += delta
    date_label.config(text=current_date.strftime("%Y-%m-%d"))
    update_subject_entries()

def update_subject_entries():
    """
    Update subject entries based on the current date.

    Returns:
    None
    """
    current_subjects = subjects_data.get(current_date, [""] * 5)
    for i in range(5):
        subject_entries[i].delete(0, "end")
        subject_entries[i].insert(0, current_subjects[i])

def go_back():
    """Move to the previous date."""
    update_date(datetime.timedelta(days=-1))

def go_forward():
    """Move to the next date."""
    update_date(datetime.timedelta(days=1))

def save_subject_entries():
    """Save entries.

    Save the entered subject entries to
    the dictionary and file.

    Returns:
    None
    """
    subjects_data[current_date] = [
        entry.get() for entry in subject_entries
    ]
    with open("db/subject_data.txt", "a") as file:
        file.write(
            f"{current_date.strftime('%Y-%m-%d')}: "
            f"{' | '.join(subjects_data[current_date])}\n"
        )

# Create the main Tkinter window.
root = Tk()
root.title("AcademicTracker - Homework Journal")
root.iconbitmap("assets/at_logo.ico")
root.geometry("1000x600")

# Initialize the current date to the current date and time.
current_date = datetime.datetime.now()

# Create and configure the label to display the current date.
date_label = Label(root, font=("Helvetica", 14))
date_label.grid(column=0, row=0, columnspan=2, padx=30)
date_label.config(text=current_date.strftime("%Y-%m-%d"))

# Labels for subject entries.
subject_1_label = Label(root, text="Subject 1", font=("Helvetica", "12"))
subject_1_label.grid(column=0, row=1)
subject_2_label = Label(root, text="Subject 2", font=("Helvetica", "12"))
subject_2_label.grid(column=0, row=2)
subject_3_label = Label(root, text="Subject 3", font=("Helvetica", "12"))
subject_3_label.grid(column=0, row=3)
subject_4_label = Label(root, text="Subject 4", font=("Helvetica", "12"))
subject_4_label.grid(column=0, row=4)
subject_5_label = Label(root, text="Subject 5", font=("Helvetica", "12"))
subject_5_label.grid(column=0, row=5)

# Entry fields for subject entries.
subject_1_entry = Entry(root, width=150)
subject_1_entry.grid(column=1, row=1)
subject_2_entry = Entry(root, width=150)
subject_2_entry.grid(column=1, row=2)
subject_3_entry = Entry(root, width=150)
subject_3_entry.grid(column=1, row=3)
subject_4_entry = Entry(root, width=150)
subject_4_entry.grid(column=1, row=4)
subject_5_entry = Entry(root, width=150)
subject_5_entry.grid(column=1, row=5)

# Load arrow icons for navigation buttons.
leftbuttonimg = PhotoImage(file="assets/left_arrow.png")
rightbuttonimg = PhotoImage(file="assets/right_arrow.png")

# Navigation buttons to go back and forward in dates.
left_button = Button(root, image=leftbuttonimg, command=go_back)
left_button.grid(column=0, row=6, columnspan=2)
right_button = Button(root, image=rightbuttonimg, command=go_forward)
right_button.grid(column=1, row=6, columnspan=2)

# Dictionary to store subject data for each date.
subjects_data = {}
subject_entries = []

# Create entry fields for each subject and load data from file.
for i in range(5):
    entry = Entry(root, width=150)
    entry.grid(column=1, row=i + 1)
    subject_entries.append(entry)
    with open("db/subject_data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(": ")
            if len(parts) == 2:
                date_str, subjects_str = parts
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                subjects = subjects_str.split(" | ")
                subjects_data[date] = subjects

# Update the subject entries based on the current date.
update_subject_entries()

# Button to save subject entries.
save_button = Button(root, text="Save", command=save_subject_entries)
save_button.grid(column=1, row=7, columnspan=2)

# Center the window and start the main event loop.
center_window(root)
root.mainloop()
