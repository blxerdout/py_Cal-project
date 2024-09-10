import tkinter as tk

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('357x420+0+0')  # Fixed spelling
        master.config(bg='gray')
        master.resizable(False, False)  # Fixed spelling

        self.equation = tk.StringVar()
        self.entry_value = ''

        # Create an Entry widget
        self.entry = tk.Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation)
        self.entry.place(x=0, y=0)

        # Example buttons for the calculator
        tk.Button(master, text='1', command=lambda: self.show(1)).place(x=0, y=50)
        tk.Button(master, text='2', command=lambda: self.show(2)).place(x=50, y=50)
        tk.Button(master, text='3', command=lambda: self.show(3)).place(x=150, y=50)
        tk.Button(master, text='4', command=lambda: self.show(4)).place(x=50, y=50)
        tk.Button(master, text='5', command=lambda: self.show(5)).place(x=50, y=50)
        tk.Button(master, text='6', command=lambda: self.show(6)).place(x=50, y=50)
        tk.Button(master, text='7', command=lambda: self.show(7)).place(x=50, y=50)
        tk.Button(master, text='8', command=lambda: self.show(8)).place(x=50, y=50)
        tk.Button(master, text='9', command=lambda: self.show(9)).place(x=50, y=50)
        tk.Button(master, text='0', command=lambda: self.show(0)).place(x=50, y=50)
        tk.Button(master, text='C', command=self.clear).place(x=100, y=50)
        tk.Button(master, text='=', command=self.solve).place(x=150, y=50)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

# Create the root window
root = tk.Tk()

# Create an instance of the Calculator class
calc = Calculator(root)

# Run the Tkinter event loop
root.mainloop()
