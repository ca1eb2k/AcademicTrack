"""This script implements a customizable timetable entry system.

The script provides an interface for users to input and
save timetable data. It consists of an array of entry boxes
arranged in a grid format.
Users can input information for up to 5 rows and 10 columns.
The data is then saved to a file named "timetableinfo.txt"
when the "Save Entries" button is clicked.

Functions:
- create_custom_entry(parent, font): Creates a custom Entry
widget with specified font and returns it.
- load_and_update_data(file_path): Loads and updates timetable
data from the specified file, populating the entry boxes if
the data is valid.

GUI Components:
- Main Tkinter window (root): The main window of the timetable
entry system.
- Entry boxes (entry_boxes): A 2D array of Entry widgets for
inputting data.
- Save Entries button (save_button): Button to save entered
data to the "timetableinfo.txt" file.

Layout:
- Entry boxes are arranged in a grid layout using the grid method.
- The Save Entries button spans all columns and is positioned
below the entry boxes.

Execution:
- The main event loop of the Tkinter application is
started using root.mainloop().
"""

import tkinter as tk

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

def create_custom_entry(parent, font):
    """Create and return a custom Entry widget."""
    entry = tk.Entry(parent, font=font, width=6)
    return entry

def load_and_update_data(file_path):
    """Load and update data.

    Load data from a file, validate its format,
    and update entry boxes accordingly.

    """
    with open(file_path, "r") as file:
        data_str = file.read()
        data_list = eval(data_str)

        if isinstance(data_list, list) and \
                len(data_list) == 5 and \
                all(isinstance(row, list) and len(row) == 10 for row in data_list):
            for row in range(5):
                for col in range(10):
                    entry = entry_boxes[row][col]
                    entry.delete(0, tk.END)
                    entry.insert(0, data_list[row][col])
        else:
            print("Error: Invalid data format.")

# Create the main Tkinter window.
root = tk.Tk()
root.geometry("1000x600")

# Define the font to be used for entry boxes.
font = ("Helvetica", 21)

# Initialize a list to store entry boxes.
entry_boxes = []

# Create entry boxes in a 5x10 grid and store them in the list.
for row in range(5):
    row_entries = []
    for col in range(10):
        entry = create_custom_entry(root, font)
        entry.grid(column=col, row=row)
        row_entries.append(entry)
    entry_boxes.append(row_entries)

# Define the data file path.
DATA_FILE = "timetableinfo.txt"

# Load and update data from the file.
load_and_update_data(DATA_FILE)

# Define a function to save the entered data.
def save_entries():
    data = []
    for row in range(5):
        row_data = []
        for col in range(10):
            entry = entry_boxes[row][col]
            entered_text = entry.get()
            row_data.append(entered_text)
        data.append(row_data)

    with open(DATA_FILE, "w") as file:
        file.write(str(data))
        print("Data saved successfully.")

# Create a button to trigger saving of the entries.
save_button = tk.Button(root, text="Save Entries", command=save_entries)
save_button.grid(columnspan=10, row=5)

# Center the window and start the main event loop.
center_window(root)
root.mainloop()
