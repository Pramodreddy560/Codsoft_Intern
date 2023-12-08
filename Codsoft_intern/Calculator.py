import tkinter as tk
from tkinter import messagebox
from tkinter import font

def button_click(number):
    # Gets the Number from User

    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def button_clear():
    """ Clear the Number in entry list"""
    entry.delete(0, tk.END)


def button_operator(operator):
    """ Gets the operator from User"""
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = operator
    f_num = float(first_number)
    entry.delete(0, tk.END)


def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)
    if math_operation == "addition":
        entry.insert(tk.END, f_num + float(second_number))
    elif math_operation == "subtraction":
        entry.insert(tk.END, f_num - float(second_number))
    elif math_operation == "multiplication":
        entry.insert(tk.END, f_num * float(second_number))
    elif math_operation == "division":
        if float(second_number) != 0:
            entry.insert(tk.END, f_num / float(second_number))
        else:
            messagebox.showerror("Error", "Division by zero is not allowed.")


# Creating the main window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="white")
window.geometry("270x350")

# font style setting
font_style = font.Font(family="Poppins", size=10)

# Creating the entry field
entry = tk.Entry(window, width=20, borderwidth=5, font=("Arial", 16), justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Creating the number buttons
button_1 = tk.Button(window, text="1", padx=20, pady=10, font=("Arial", 12), command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=20, pady=10, font=("Arial", 12), command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=20, pady=10, font=("Arial", 12), command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=20, pady=10, font=("Arial", 12), command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=20, pady=10, font=("Arial", 12), command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=20, pady=10, font=("Arial", 12), command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=20, pady=10, font=("Arial", 12), command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=20, pady=10, font=("Arial", 12), command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=20, pady=10, font=("Arial", 12), command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=20, pady=10, font=("Arial", 12), command=lambda: button_click(0))

button_1.grid(row=3, column=0, pady=5)
button_2.grid(row=3, column=1, pady=5)
button_3.grid(row=3, column=2, pady=5)
button_4.grid(row=2, column=0, pady=5)
button_5.grid(row=2, column=1, pady=5)
button_6.grid(row=2, column=2, pady=5)
button_7.grid(row=1, column=0, pady=5)
button_8.grid(row=1, column=1, pady=5)
button_9.grid(row=1, column=2, pady=5)
button_0.grid(row=4, column=0, pady=5)

# Creating the operator buttons
button_add = tk.Button(window, text="+", padx=19, pady=10, font=("Arial", 12),
                       command=lambda: button_operator("addition"))
button_subtract = tk.Button(window, text="-", padx=20, pady=10, font=("Arial", 12),
                            command=lambda: button_operator("subtraction"))
button_multiply = tk.Button(window, text="*", padx=20, pady=10, font=("Arial", 12),
                            command=lambda: button_operator("multiplication"))
button_divide = tk.Button(window, text="/", padx=20, pady=10, font=("Arial", 12),
                          command=lambda: button_operator("division"))
button_equal = tk.Button(window, text="=", padx=19, pady=10, font=("Arial", 12), command=button_equal)
button_clear = tk.Button(window, text="C", padx=18, pady=10, font=("Arial", 12), command=button_clear)

button_add.grid(row=1, column=3, pady=5)
button_subtract.grid(row=2, column=3, pady=5)
button_multiply.grid(row=3, column=3, pady=5)
button_divide.grid(row=4, column=3, pady=5)
button_equal.grid(row=4, column=2, pady=5)
button_clear.grid(row=4, column=1, pady=5)

Credit_label = tk.Label(window, text="Code By Pramod", font=font_style)
Credit_label.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Starting the GUI
window.mainloop()

# Code by Pramod