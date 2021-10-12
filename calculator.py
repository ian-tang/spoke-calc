from tkinter import Tk, Entry, Button, END

# create new window
root = Tk()
root.title("Calculator")

# create and place numbers field
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

# define button actions
def button_number(num):
    e.insert(END, num)

def button_operation(op):
    global stored_value
    global operation
    stored_value = e.get()
    e.delete(0, END)
    operation = op

def button_clear():
    e.delete(0, END)
    
def button_equal():
    current_value = e.get()
    e.delete(0, END)
    if operation == "add":
        e.insert(0, int(stored_value) + int(current_value))
    if operation == "subtract":
        e.insert(0, int(stored_value) - int(current_value))
    if operation == "multiply":
        e.insert(0, int(stored_value) * int(current_value))
    if operation == "divide":
        e.insert(0, int(stored_value) / int(current_value))


# define number buttons
button_1 = Button(root, text="1", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_number(1))
button_2 = Button(root, text="2", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_number(2))
button_3 = Button(root, text="3", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_number(3))
button_4 = Button(root, text="4", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_number(4))
button_5 = Button(root, text="5", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_number(5))
button_6 = Button(root, text="6", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_number(6))
button_7 = Button(root, text="7", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_number(7))
button_8 = Button(root, text="8", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_number(8))
button_9 = Button(root, text="9", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_number(9))
button_0 = Button(root, text="0", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_number(0))

# define operator buttons
button_add = Button(root, text="+", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_operation("add"))
button_sub = Button(root, text="-", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_operation("subtract"))
button_multi = Button(root, text="*", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_operation("multiply"))
button_div = Button(root, text="/", padx=40, pady=15, borderwidth=4, font="terminal", command=lambda: button_operation("divide"))
button_equal = Button(root, text="=", padx = 96, pady=15, borderwidth=4, font="terminal", command=button_equal)
button_clear = Button(root, text="Clear", padx = 72, pady=15, borderwidth=4, font="terminal", command=button_clear)

# place number buttons in grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

# place operator buttons in grid
button_add.grid(row=5, column=0)
button_sub.grid(row=6, column=0)
button_multi.grid(row=6, column=1)
button_div.grid(row=6, column=2)
button_equal.grid(row=4, column=1, columnspan=2)
button_clear.grid(row=5, column=1, columnspan=2)

# run widget
root.mainloop()