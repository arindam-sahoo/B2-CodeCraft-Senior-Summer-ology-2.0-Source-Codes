# Tkinter
# Tkinter is a Python library that is used for creating GUIs (Graphical User Interfaces)
# 'User Interfaces' are used to display information to the user.

from tkinter import *

exp = ""

def btnPress(num):
  global exp
  exp = exp + str(num)
  eq.set(exp)

def btnBkSp():
  global exp
  exp = exp[:-1]
  eq.set(exp)

def btnEqual():
  try:
    global exp
    res = str(eval(exp))
    eq.set(res)
    exp = res
  except:
    eq.set("ERROR")
    exp = ""

def btnClr():
  global exp
  exp = ''
  eq.set(exp)

def btnPercent():
  # 25% of 120 = (25*120) / 100 = 30
  try:
    global exp
    if '*' in exp:
      res = str(eval(exp)/100)
    eq.set(res)
    exp = res
  except:
    eq.set('ERROR')
    exp = ''
  
# Creating the root window
root = Tk()
# Setting the title of the window
root.title("CodeCraft Calculator")
# Assigning the Icon
root.iconbitmap('./Calculator.ico')
# Setting the dimensions of the window
# root.geometry("300x300")
# Disable maximizing the window
root.resizable(False, False)

# Creating a label
lbl = Label(root, text="CodeCraft Calculator", font=('Helvetica', 20, 'bold'))
lbl.grid(row=0, column=0, columnspan=4)

# Creating the display for the calculator
eq = StringVar()
disp = Label(root, textvariable=eq, font=('Helvetica', 30), bg='white', anchor='e', width=14, bd=2, relief=SOLID)
disp.grid(row=1, column=0, columnspan=4)
eq.set('0')

# Creating the buttons
btnOff = Button(root, text='OFF', height=2, width=6, font=('Helvetica', 14, 'bold'), bg='black', fg='orange', command=root.destroy)
btnOff.grid(row=2, column=0)
btnClr = Button(root, text=' C ', height=2, width=6, font=('Helvetica', 14, 'bold'), bg='black', fg='orange', command=btnClr)
btnClr.grid(row=2, column=1)
btnPer = Button(root, text=' % ', height=2, width=6, font=('Helvetica', 14, 'bold'), bg='black', fg='orange', command=btnPercent)
btnPer.grid(row=2, column=2)
btnDiv = Button(root, text=' / ', height=2, width=6, font=('Helvetica', 14, 'bold'), bg='orange', command=lambda:btnPress('/'))
btnDiv.grid(row=2, column=3)

btn7 = Button(root, text=' 7 ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress(7))
btn7.grid(row=3, column=0)
btn8 = Button(root, text=' 8 ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress(8))
btn8.grid(row=3, column=1)
btn9 = Button(root, text=' 9 ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress(9))
btn9.grid(row=3, column=2)
btnMul = Button(root, text=' X ', height=2, width=6, font=('Helvetica', 14, 'bold'), bg='orange', command=lambda:btnPress('*'))
btnMul.grid(row=3, column=3)

btn4 = Button(root, text=' 4 ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress(4))
btn4.grid(row=4, column=0)
btn5 = Button(root, text=' 5 ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress(5))
btn5.grid(row=4, column=1)
btn6 = Button(root, text=' 6 ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress(6))
btn6.grid(row=4, column=2)
btnSub = Button(root, text=' - ', height=2, width=6, font=('Helvetica', 14, 'bold'), bg='orange', command=lambda:btnPress('-'))
btnSub.grid(row=4, column=3)

btn1 = Button(root, text=' 1 ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress(1))
btn1.grid(row=5, column=0)
btn2 = Button(root, text=' 2 ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress(2))
btn2.grid(row=5, column=1)
btn3 = Button(root, text=' 3 ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress(3))
btn3.grid(row=5, column=2)
btnSum = Button(root, text=' + ', height=2, width=6, font=('Helvetica', 14, 'bold'), bg='orange', command=lambda:btnPress('+'))
btnSum.grid(row=5, column=3)

btn0 = Button(root, text=' 0 ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress(0))
btn0.grid(row=6, column=0)
btnDot = Button(root, text=' . ', height=2, width=6, font=('Helvetica', 14, 'bold'), command=lambda:btnPress('.'))
btnDot.grid(row=6, column=1)
btnBks = Button(root, text=' << ', height=2, width=6, font=('Helvetica', 14, 'bold'), bg='black', fg='orange', command=btnBkSp)
btnBks.grid(row=6, column=2)
btnEql = Button(root, text=' = ', height=2, width=6, font=('Helvetica', 14, 'bold'), bg='orange', command=btnEqual)
btnEql.grid(row=6, column=3)

root.mainloop()
