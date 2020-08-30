from tkinter import *
import Bisection.bisection as bs
import numpy as np
import matplotlib.pyplot as plt
from gui.convert2function import string2func

table = None

root = Tk()
root.title('Numerical Anaysis')
#root.iconbitmap('icon.ico')
root.geometry("410x400")

# Destroy window
def close_window():
    root.destroy()

# Export to txt file
def export_txt():
    global table
    with open('file.txt', 'w') as w:
        w.write(str(table))

# plot function
def graph(f, a, b, p_x, f_x):
    func = string2func(f)
    x = np.linspace(a, b, 250)    
    plt.plot(x, func(x))
    plt.plot(p_x, f_x)
    plt.plot(p_x[-1], f_x[-1], 'ro')
    plt.annotate("P", (p_x[-1], f_x[-1]))
    plt.legend(["Function", "Iteration"])
    plt.xlim(a, b)
    plt.show()


# Create submit Fucntion for Bisection
def bisection():
    global table    
    f = g = function.get()
    a = lower_limit.get()
    b = upper_limit.get()
    tol = tolerance.get()
    n = iteration.get()
    
    p, table, p_x, f_x = bs.bisection(f, float(a), float(b), float(tol), int(n))
    
    result_text = "The solution to the equation {} = 0 \nis {}".format(f, p)
    result_label = Label(root, text=result_text)
    result_label.grid(row=9, column=0, columnspan=2)

    export_btn["state"] = NORMAL 

    function.delete(0, END)
    lower_limit.delete(0, END)
    upper_limit.delete(0, END)
    tolerance.delete(0, END)
    iteration.delete(0, END)

    graph(g, float(a), float(b), p_x, f_x)    

# Create Text Boxes
function = Entry(root, width=30)
function.grid(row=0, column=1, padx=20)

lower_limit = Entry(root, width=30)
lower_limit.grid(row=1, column=1, padx=20)

upper_limit = Entry(root, width=30)
upper_limit.grid(row=2, column=1, padx=20)

tolerance = Entry(root, width=30)
tolerance.grid(row=3, column=1, padx=20)

iteration = Entry(root, width=30)
iteration.grid(row=4, column=1, padx=20)

# create Text Box Labels

function_label = Label(root, text="Function")
function_label.grid(row=0, column=0)

lower_limit_label = Label(root, text="Lower limit")
lower_limit_label.grid(row=1, column=0)

upper_limit_label = Label(root, text="Upper limit")
upper_limit_label.grid(row=2, column=0)

tolerance_label = Label(root, text="Tolerance")
tolerance_label.grid(row=3, column=0)

iteration_label = Label(root, text="Iterations")
iteration_label.grid(row=4, column=0)

# create Submit Button
submit_btn = Button(root, text="Find Solution", command=bisection)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create Submit Button
close_btn = Button(root, text="Close Window", command=close_window)
close_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# create Export Button
export_btn = Button(root, text="Export results", command=export_txt, state=DISABLED)
export_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


root.mainloop()