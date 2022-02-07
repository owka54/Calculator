from lib2to3.pgen2.token import PLUS
from tkinter import *
from tkinter import Tk


calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# Creating the window
root = Tk()
root.title("Calculator")
root.geometry("300x285")

# Creating the calculator display
text_result = Text(root, height=2, width=16, font=("Ariel", 24), background="black", foreground="white")
text_result.grid(columnspan=5)


# Creating the buttons
btn1 = Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Ariel", 14, "bold"))
btn1.grid(row=4, column=1)
root.bind("1", lambda e: add_to_calculation(1))
btn2 = Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Ariel", 14, "bold"))
btn2.grid(row=4, column=2)
root.bind("2", lambda e: add_to_calculation(2))
btn3 = Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Ariel", 14, "bold"))
btn3.grid(row=4, column=3)
root.bind("3", lambda e: add_to_calculation(3))
btn4 = Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Ariel", 14, "bold"))
btn4.grid(row=3, column=1)
root.bind("4", lambda e: add_to_calculation(4))
btn5 = Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Ariel", 14, "bold"))
btn5.grid(row=3, column=2)
root.bind("5", lambda e: add_to_calculation(5))
btn6 = Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Ariel", 14, "bold"))
btn6.grid(row=3, column=3)
root.bind("6", lambda e: add_to_calculation(6))
btn7 = Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Ariel", 14, "bold"))
btn7.grid(row=2, column=1)
root.bind("7", lambda e: add_to_calculation(7))
btn8 = Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Ariel", 14, "bold"))
btn8.grid(row=2, column=2)
root.bind("8", lambda e: add_to_calculation(8))
btn9 = Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Ariel", 14, "bold"))
btn9.grid(row=2, column=3)
root.bind("9", lambda e: add_to_calculation(9))
btn0 = Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Ariel", 14, "bold"))
btn0.grid(row=5, column=1)
root.bind("0", lambda e: add_to_calculation(0))

btndot = Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Ariel", 14, "bold"))
btndot.grid(row=5, column=2)
root.bind(".", lambda e: add_to_calculation("."))

btnadd = Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Ariel", 14, "bold"))
btnadd.grid(row=1, column=4)
root.bind("+", lambda e: add_to_calculation("+"))
btnminus = Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Ariel", 14, "bold"))
btnminus.grid(row=2, column=4)
root.bind("-", lambda e: add_to_calculation("-"))
btnmul = Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Ariel", 14, "bold"))
btnmul.grid(row=3, column=4)
root.bind("*", lambda e: add_to_calculation("*"))
btndiv = Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Ariel", 14, "bold"))
btndiv.grid(row=4, column=4)
root.bind("/", lambda e: add_to_calculation("/"))

btnopen = Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Ariel", 14, "bold"))
btnopen.grid(row=1, column=2)
root.bind("<(>", lambda e: add_to_calculation("("))
btnclose = Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Ariel", 14, "bold"))
btnclose.grid(row=1, column=3)
root.bind("<)>", lambda e: add_to_calculation(")"))

btnequals = Button(root, text="=", command=lambda: evaluate_calculation(), width=11, font=("Ariel", 14, "bold"))
btnequals.grid(row=5, column=3, columnspan=2)
root.bind("<Return>", lambda e: evaluate_calculation())
btnclear = Button(root, text="C", command=lambda: clear_field(), width=5, font=("Ariel", 14, "bold"), foreground="red")
btnclear.grid(row=1, column=1)
root.bind("<Delete>", lambda e: clear_field())
root.bind("<BackSpace>", lambda e: clear_field())

root.mainloop()