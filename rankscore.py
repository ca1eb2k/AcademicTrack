"""This script implements a GUI-based Rank Score Calculator for the app.

It uses the tkinter library to create an interface where
users can input their achieved, merit, and excellence scores.
Upon clicking the 'Calculate' button, the script computes
the rank score based on the provided scores and displays the result.

Functions:
- calculate_score(): Calculates and displays the rank score
based on input values.

GUI Components:
- Main Tkinter window (root): The main window of the calculator.
- Labels for headings and score display (heading_label,
achieved_label, merit_label, excellence_label, score_label).
- Entry boxes for input (achieved_entry, merit_entry, excellence_entry).
- Button to trigger score calculation (calculate_button).

Layout:
- Labels, entry boxes, and buttons are positioned in a grid
layout using the grid method.

Execution:
- The main event loop of the Tkinter application is started
using root.mainloop().
"""

# Import necessary libraries.
import tkinter as tk
from tkinter import messagebox

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

def calculate_score():
    """
    Calculate and display rank score based on input values.

    This function retrieves input values, performs calculations,
    and displays the result.

    Returns:
    None
    """
    try:
        # Convert the input values to floats.
        achieved = float(achieved_entry.get())
        merit = float(merit_entry.get())
        excellence = float(excellence_entry.get())
    except ValueError:
        # Display an error message for invalid input values.
        messagebox.showerror("Error", "Enter valid numerical values!")
        return

    # Calculate total score before multiplication.
    total_before_multiplication = achieved + merit + excellence

    # Check if total before multiplication exceeds 80.
    if total_before_multiplication > 80:
        messagebox.showerror("Error", "Total score exceeds 80!")
        return

    # Calculate total score based on weights and display the result.
    total_score = (achieved * 2) + (merit * 3) + (excellence * 4)
    score_label.config(text="Your Rank Score: {:.2f}".format(total_score))

# Create main Tkinter window.
root = tk.Tk()
root.title("AcademicTracker - Rank Score Calculator")
root.iconbitmap("assets/at_logo.ico")
root.geometry("1000x600")

# GUI components setup.
heading_label = tk.Label(root, text="Rank Score Calculator",
                         font=("Helvetica", 24, "bold"))
heading_label.grid(row=0, column=2, padx=320, columnspan=5)

empty_label = tk.Label(root)
empty_label.grid(row=1, column=2)

achieved_label = tk.Label(root, text="Achieved",
                          font=("Helvetica", 15, "italic"))
achieved_label.grid(row=2, column=3, padx=20)

merit_label = tk.Label(root, text="Merit", font=("Helvetica", 15, "italic"))
merit_label.grid(row=2, column=4, padx=20)

excellence_label = tk.Label(root, text="Excellence",
                            font=("Helvetica", 15, "italic"))
excellence_label.grid(row=2, column=5, padx=20)

achieved_entry = tk.Entry(root)
achieved_entry.grid(row=3, column=3)

merit_entry = tk.Entry(root)
merit_entry.grid(row=3, column=4)

excellence_entry = tk.Entry(root)
excellence_entry.grid(row=3, column=5)

empty_label = tk.Label(root)
empty_label.grid(row=4, column=4)

calculate_button = tk.Button(root, text="Calculate",
                             font=40, command=calculate_score)
calculate_button.grid(row=5, column=4)

empty_label = tk.Label(root)
empty_label.grid(row=6, column=4)

score_label = tk.Label(root, font=("Helvetica", 15, "italic"))
score_label.grid(row=7, column=4)

# Center the window on the screen and start the main event loop.
center_window(root)
root.mainloop()
