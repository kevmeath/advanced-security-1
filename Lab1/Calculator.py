import tkinter as tk
import re

# string of numbers and operators to help with input validation
numbers = '0123456789'
operators = '/*-+'


# Application
class Application(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        # Set equal weight for all grid cells
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

        # Allow widgets to scale with window size
        self.pack(fill='both', expand=True)

        # StringVar for holding user input
        self.input = tk.StringVar()
        self.input.set('')

        # Label for displaying user input
        tk.Label(self, textvariable=self.input).grid(row=0, column=0, columnspan=5, sticky='NESW')

        self.create_buttons()

    # creates all gui buttons
    def create_buttons(self):
        # numbers 1-9
        for i in range(3):
            for j in range(3):
                index = (i+j+1)+2*i
                tk.Button(self, text=str(index), command=lambda char=index: self.enter_char(str(char))).grid(row=3-i, column=j, padx=5, pady=5, sticky='NESW')

        # 0 button
        tk.Button(self, text='0', command=lambda: self.enter_char('0')).grid(row=4, column=0, padx=5, pady=5, sticky='NESW')

        # Operator buttons
        for i in range(4):
            tk.Button(self, text=str(operators[i]), command=lambda char=operators[i]: self.enter_char(str(char))).grid(row=i+1, column=3, padx=5, pady=5, sticky='NESW')

        # Decimal button
        tk.Button(self, text=str('.'), command=lambda: self.enter_char('.')).grid(row=4, column=1, padx=5, pady=5, sticky='NESW')

        # Equals/Answer button
        tk.Button(self, text='=', command=self.answer).grid(row=4, column=4, padx=5, pady=5, sticky='NESW')

        # Backspace button
        tk.Button(self, text='\u232b', command=self.backspace).grid(row=1, column=4, padx=5, pady=5, sticky='NESW')

        # Clear button
        tk.Button(self, text='C', command=self.clear).grid(row=2, column=4, padx=5, pady=5, sticky='NESW')

    # Returns the last character entered
    def get_last_char(self):
        if not self.input.get():
            return ''
        else:
            return self.input.get()[-1]

    # Appends a character to input. Called when a number or operator button is pressed
    def enter_char(self, nextInput: str):
        # The first character must be a number
        # There can be only one decimal per number
        # An operator must be surrounded by zeros
        if (nextInput in numbers) or\
                (nextInput == '.' and '.' not in re.split('[/*-+]', self.input.get())[-1]) or\
                (nextInput in operators and self.get_last_char() not in operators+'.'):
            self.input.set(self.input.get() + nextInput)

    # Removes the last character of input. Called when backspace is pressed
    def backspace(self):
        if self.get_last_char():
            self.input.set(self.input.get()[:-1])

    # Clears input. Called when clear button is pressed
    def clear(self):
        if self.get_last_char():
            self.input.set('')

    # Evaluates the expression in the input box. Called when equals button is pressed
    def answer(self):
        if self.get_last_char() in numbers:
            self.input.set(eval(self.input.get()))


# Set up main window
root = tk.Tk()
root.title('Calculator')
root.geometry('240x240')
app = Application(parent=root)
app.mainloop()
