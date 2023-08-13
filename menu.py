import subprocess
from tkinter import Tk, Button, PhotoImage, Label

# Create the main Tkinter window
root = Tk()

# Set the window size, title, and icon
root.geometry("1000x600")
root.title("AcademicTracker - Home")

# Makes a welcome label using helvetica font and put it in the window
welcome_label = Label(root, text="Welcome!", font=("Arial", 36))
welcome_label.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Load images for buttons
timetableimg = PhotoImage(file="timetable.png")
homeworkimg = PhotoImage(file="homework.png")
rankscoreimg = PhotoImage(file="rankscore.png")


rankscore_button = Button(root, image=rankscoreimg)
timetable_button = Button(root, image=timetableimg)
homework_button = Button(root, image=homeworkimg)

timetable_button.grid(row=2, column=2)
homework_button.grid(row=3, column=2)
rankscore_button.grid(row=4, column=2)


root.mainloop()
