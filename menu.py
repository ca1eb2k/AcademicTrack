# import libraries
import os
import subprocess
from tkinter import Tk, Button, PhotoImage, Label, font

# Function to open a Python program using subprocess
def open_program(file_path):
    subprocess.call(['python', file_path])

# Create the main Tkinter window
root = Tk()

# Set the window size, title, and icon
root.geometry("1000x600")
root.title("AcademicTracker - Home")
root.iconbitmap("assets/at_logo.ico")

# Makes a welcome label using helvetica font and put it in the window
welcome_label = Label(root, text="Welcome to AcademicTracker!", font=("Arial", 36))
welcome_label.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Load images for buttons
timetableimg = PhotoImage(file="assets/timetable.png")
homeworkimg = PhotoImage(file="assets/homework.png")
rankscoreimg = PhotoImage(file="assets/rankscore.png")

# Create buttons with images and connect the buttons to opening their programs, lambda used only when button clicked not when widget made
rankscore_button = Button(root, image=rankscoreimg, command=lambda: open_program("rankscore.py"))
timetable_button = Button(root, image=timetableimg, command=lambda: open_program("timetable.py"))
homework_button = Button(root, image=homeworkimg, command=lambda: open_program("homework_journal.py"))

# Place buttons in the grid layout
timetable_button.grid(row=2, column=2)
homework_button.grid(row=3, column=2)
rankscore_button.grid(row=4, column=2)

root.mainloop()
