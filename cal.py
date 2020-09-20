from tkinter import *

root = Tk()

root.title("Calculator")

root.geometry('300x450+300+100')
root.resizable(0,0)

# display frame

display = Label(
    text = 'Label',
    anchor =  E,
    bg = 'white',
    padx = 10,
    font = ("Vendara", 22)
)
display.pack(expand = True, fill = 'both')

# clear btn frame

clear = Frame(root, bg = 'white')
clear.pack(expand = True, fill = 'both')

clearBtn = Button(
    
    clear,
    bg = '#88fce1',
    text = "CE",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
clearBtn.pack(side = LEFT, expand = True , fill = 'both')


# button row1 frame

btnRow1 = Frame(root, bg = 'gray')
btnRow1.pack(expand = True, fill = 'both')


# button row2 frame

btnRow2 = Frame(root, bg = 'gray')
btnRow2.pack(expand = True, fill = 'both')

# button row3 frame

btnRow3 = Frame(root, bg = 'gray')
btnRow3.pack(expand = True, fill = 'both')

# button row4 frame

btnRow4 = Frame(root, bg = 'gray')
btnRow4.pack(expand = True, fill = 'both')


# Buttons
# 4TH BTN ROW
pointBtn = Button(
    btnRow4,
    text = ".",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
pointBtn.pack(side = LEFT, expand = True , fill = 'both')

zeroBtn = Button(
    btnRow4,
    text = "0",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
zeroBtn.pack(side = LEFT, expand = True , fill = 'both')

equalBtn = Button(
    btnRow4,
    text = "=",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
equalBtn.pack(side = LEFT, expand = True , fill = 'both')

plusBtn = Button(
    btnRow4,
    text = "+",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
plusBtn.pack(side = LEFT, expand = True , fill = 'both')

# 3rd BTN ROW
btn1st = Button(
    btnRow3,
    text = "1",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
btn1st.pack(side = LEFT, expand = True , fill = 'both')

btn2nd = Button(
    btnRow3,
    text = "2",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
btn2nd.pack(side = LEFT, expand = True , fill = 'both')

btn3rd = Button(
    btnRow3,
    text = "3",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
btn3rd.pack(side = LEFT, expand = True , fill = 'both')

minusBtn = Button(
    btnRow3,
    text = "-",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
minusBtn.pack(side = LEFT, expand = True , fill = 'both')

# 2nd BTN ROW
btn4th = Button(
    btnRow2,
    text = "4",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
btn4th.pack(side = LEFT, expand = True , fill = 'both')

btn5th = Button(
    btnRow2,
    text = "5",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
btn5th.pack(side = LEFT, expand = True , fill = 'both')

btn6th = Button(
    btnRow2,
    text = "6",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
btn6th.pack(side = LEFT, expand = True , fill = 'both')

multipleBtn = Button(
    btnRow2,
    text = "*",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
multipleBtn.pack(side = LEFT, expand = True , fill = 'both')

# 2nd BTN ROW
btn7th = Button(
    btnRow1,
    text = "7",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
btn7th.pack(side = LEFT, expand = True , fill = 'both')

btn8th = Button(
    btnRow1,
    text = "8",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
btn8th.pack(side = LEFT, expand = True , fill = 'both')

btn9th = Button(
    btnRow1,
    text = "9",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
btn9th.pack(side = LEFT, expand = True , fill = 'both')

divisionBtn = Button(
    btnRow1,
    text = "/",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0
)
divisionBtn.pack(side = LEFT, expand = True , fill = 'both')

root.mainloop()
