import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression entered by the user
def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)  # Evaluate the mathematical expression
        entry.delete(0, tk.END)  # Clear the input field
        entry.insert(tk.END, str(result))  # Insert the result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")  # Error message for invalid input

# Function to clear the input field
def clear_input():
    entry.delete(0, tk.END)

# Creating the main window
window = tk.Tk()
window.title("Simple Calculator")

# Input field
entry = tk.Entry(window, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Button click function to append text to input field
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Create number and operation buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, width=10, height=2, command=evaluate_expression)
    else:
        button = tk.Button(window, text=text, width=10, height=2, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(window, text='Clear', width=44, height=2, command=clear_input)
clear_button.grid(row=5, column=0, columnspan=4)

# Start the Tkinter event loop
window.mainloop()

