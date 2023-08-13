"""This file serves as the main interface for the app's homescreen.

It uses the tkinter library to create a graphical user interface (GUI)
with buttons that provide access to different features of the application.
The main window contains buttons for the timetable, homework journal,
and rank/score tracking features. When a button is clicked, it opens
the corresponding Python program using subprocess.

Functions:
- open_program(file_path): Opens a Python program using the
subprocess module.

GUI Components:
- Main Tkinter window (root): The main window of the application.
- Welcome label (welcome_label): Displays a welcoming message
to the user.
- Buttons for features: Timetable, Homework Journal, Rank/Score
Tracking (timetable_button, homework_button, rankscore_button).

Images:
- Images for buttons are loaded from image files:
"assets/timetable.png", "assets/homework.png", "assets/rankscore.png".

Layout:
- The welcome label and buttons are positioned
in a grid layout using the grid method.

Execution:
- The main event loop of the Tkinter application
is started using root.mainloop().

"""

import subprocess
from tkinter import Tk, Button, PhotoImage, Label


def open_program(file_path):
    """
    Open a Python program using subprocess.

    Parameters:
    file_path (str): Path to the Python program file.

    Returns:
    None
    """
    subprocess.call(['python', file_path])


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


# Create the main Tkinter window.
root = Tk()

# Set the window size, title, and icon.
root.geometry("1000x600")
root.title("AcademicTracker - Home")
root.iconbitmap("assets/at_logo.ico")

# Makes a welcome label using helvetica font and put it in the window.
welcome_label = Label(root, text="Welcome!", font=("Arial", 36))
welcome_label.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Load images for buttons.
timetableimg = PhotoImage(file="assets/timetable.png")
homeworkimg = PhotoImage(file="assets/homework.png")
rankscoreimg = PhotoImage(file="assets/rankscore.png")

# Create buttons with images and connect the buttons to opening
# their programs, lambda used only when button clicked not when widget made.
rankscore_button = Button(root, image=rankscoreimg,
                          command=lambda: open_program("rankscore.py"))
timetable_button = Button(root, image=timetableimg,
                          command=lambda: open_program("timetable.py"))
homework_button = Button(root, image=homeworkimg,
                         command=lambda: open_program("homework_journal.py"))

# Place buttons in the grid layout.
timetable_button.grid(row=2, column=2)
homework_button.grid(row=3, column=2)
rankscore_button.grid(row=4, column=2)

center_window(root)

# Start the main event loop of the Tkinter application..
root.mainloop()
