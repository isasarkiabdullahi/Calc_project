import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Input field (Text widget)
calculation_field = tk.Text(root, height=2, width=24, font=("Arial", 18))
calculation_field.pack(pady=10)

# Function to insert text into the input field
def insert_to_field(value):
    calculation_field.insert(tk.END, value)

# Function to clear the input field
def clear_field():
    calculation_field.delete("1.0", tk.END)

# Function to evaluate the expression
def evaluate_calculation():
    try:
        expression = calculation_field.get("1.0", tk.END).strip()
        result = eval(expression)
        clear_field()
        calculation_field.insert("1.0", str(result))
    except:
        clear_field()
        calculation_field.insert("1.0", "Error")

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('C',)
]

# Create buttons and place them in a grid
button_frame = tk.Frame(root)
button_frame.pack()

for row_index, row_values in enumerate(buttons):
    for col_index, button_text in enumerate(row_values):
        if button_text == '=':
            button = tk.Button(button_frame, text=button_text, height=2, width=5,
                               command=evaluate_calculation, font=("Arial", 14))
        elif button_text == 'C':
            button = tk.Button(button_frame, text=button_text, height=2, width=24,
                               command=clear_field, font=("Arial", 14))
            button.grid(row=row_index, column=0, columnspan=4, pady=5)
            break
        else:
            button = tk.Button(button_frame, text=button_text, height=2, width=5,
                               command=lambda val=button_text: insert_to_field(val), font=("Arial", 14))
        button.grid(row=row_index, column=col_index, padx=5, pady=5)

# Run the application
root.mainloop()
