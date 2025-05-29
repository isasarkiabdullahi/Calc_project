
---

# Simple Calculator 🧮

**Video Demo:** [Watch Demo here](https://youtu.be/pi5AO9ST9oI)

## Description

Simple Calculator is a basic calculator app developed using Python and Tkinter for the CS50 final project submission. It allows users to perform simple arithmetic operations such as addition, subtraction, multiplication, and division through an intuitive graphical interface.

## Features 🚀

* **Addition, Subtraction, Multiplication, Division:** Supports basic arithmetic operations.
* **Decimal Support:** Perform calculations with decimal numbers.
* **Clear Button (`C`):** Clears the input field for new calculations.
* **Responsive UI:** Clean layout with clearly labeled buttons and a large input display.
* **Error Handling:** Displays "Error" for invalid inputs.
* **Keyboard-Free Interaction:** Fully functional using on-screen buttons.

## Install Dependencies

Ensure you have Python 3 installed on your system. You can check your Python version with:

```bash
python --version
```

Tkinter comes pre-installed with Python 3, so no additional installations are required.

## How to Run 🏃‍♂️

1. Clone the repository:

```bash
git clone https://github.com/yourusername/simple-calculator.git
cd simple-calculator
```

2. Run the application:

```bash
python calculator.py
```

The calculator window will open, ready for you to start calculating!

## How to Use 🧑‍💻

* Click the on-screen buttons to enter numbers and operators.
* Press the **`=`** button to evaluate the expression.
* Press the **`C`** button to clear the input field.
* Perform calculations like:

  * `5 + 3`
  * `10 / 2`
  * `7.5 * 4`

## Folder Structure 📁

```
simple-calculator/
├── calculator.py     # Main application script
└── README.md         # Project documentation
```

## Features Explained 📝

### GUI Layout

The calculator uses Tkinter’s grid layout system for a familiar calculator look and feel, with buttons for numbers, operators, and actions.

### Evaluation Logic

The calculator uses Python’s `eval()` function to process arithmetic expressions entered into the input field. While suitable for this simple application, `eval()` should be avoided in real-world applications with untrusted input.

### Error Handling

Invalid inputs such as incomplete expressions trigger an "Error" message in the input field, allowing users to reset and try again.

## Future Enhancements 🌟

* Add support for keyboard input.
* Include more advanced mathematical functions (square root, exponents, etc.).
* Implement history tracking for past calculations.
* Refine the interface with custom themes and colors.

## Contributing 🤝

Feel free to fork this repository and contribute improvements or new features. Open a pull request with your suggestions or fixes!

---

