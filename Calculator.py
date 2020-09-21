import tkinter
from tkinter import *

root = Tk()

root.title("Calculator")

root.geometry('300x450+300+100')
root.resizable(0,0)

previousVal = 0
next = ''
opertator = ""

# display frame
data = StringVar()
display = Label(
    root,
    text = '',
    textvariable = data,
    anchor =  E,
    bg = 'white',
    padx = 10,
    font = ("Vendara", 22)
)
display.pack(expand = True, fill = 'both')

# Btn Click functions
val = ''
def btnclick1():
    global val
    val = val + '1' 
    data.set(val)

def btnclick2():
    global val
    val = val + '2' 
    data.set(val)
    
def btnclick3():
    global val
    val = val + '3' 
    data.set(val)
    
def btnclick4():
    global val
    val = val + '4' 
    data.set(val)

def btnclick5():
    global val
    val = val + '5' 
    data.set(val)

def btnclick6():
    global val
    val = val + '6' 
    data.set(val)

def btnclick7():
    global val
    val = val + '7' 
    data.set(val)

def btnclick8():
    global val
    val = val + '8' 
    data.set(val)

def btnclick9():
    global val
    val = val + '9' 
    data.set(val)

def btnclick0():
    global val
    val = val + '0' 
    data.set(val)

def btnclickClear():
    global val
    val = '' 
    data.set(val)

def btnclickBack():
    global val
    if val == "Error":
        val = ''
    else:
        val = val[0:-1] 
    data.set(val)

def btnclickPoint():
    global val
    if val == "":
        val = "0"+"."
    else: 
        val = val+ '.' 
    data.set(val)

def operatorClickDivision():
    global val
    global previousVal
    global next
    opt = ""
    optPresent = False
    
    for i in range(0,len(val)):
        if val[i] == "+":
            optPresent = True
            previousVal = val.split("+")[0]
            next = val.split("+")[1]
            opt = "+"
            break
        elif val[i] == "-":
            optPresent = True
            previousVal = val.split("-")[0]
            next = val.split("-")[1]
            opt = "-"
            break
        elif val[i] == "*":
            optPresent = True
            previousVal = val.split("*")[0]
            next = val.split("*")[1]
            opt = "*"
            break
        elif val[i] == "/":
            optPresent = True
            previousVal = val.split("/")[0]
            next = val.split("/")[1]
            opt = "/"
            break

    if optPresent == True:
        val1 = float(previousVal)
        val2 = float(next)
        if opt == "+":
            val = round(val1 + val2,5)
            val = str(val)
            val = val + "/"
        elif opt == "-":
            val = round(val1 - val2,5)
            val = str(val)
            val = val + "/"
        elif opt == "*":
            val = round(val1 * val2,5)
            val = str(val)
            val = val + "/"
        elif opt == "/":
            val = round(val1 / val2, 5)
            val = str(val)
            val = val + "/"
        data.set(val)
    else:
        if val == "":
            val  = '0' + "/"
        else:
            val = val + '/'
        data.set(val)




def operatorClickMultiplication():
    global val
    global previousVal
    global next
    opt = ""
    optPresent = False
    
    for i in range(0,len(val)):
        if val[i] == "+":
            optPresent = True
            previousVal = val.split("+")[0]
            next = val.split("+")[1]
            opt = "+"
            break
        elif val[i] == "-":
            optPresent = True
            previousVal = val.split("-")[0]
            next = val.split("-")[1]
            opt = "-"
            break
        elif val[i] == "*":
            optPresent = True
            previousVal = val.split("*")[0]
            next = val.split("*")[1]
            opt = "*"
            break
        elif val[i] == "/":
            optPresent = True
            previousVal = val.split("/")[0]
            next = val.split("/")[1]
            opt = "/"
            break

    if optPresent == True:
        val1 = float(previousVal)
        val2 = float(next)
        if opt == "+":
            val = round(val1 + val2,5)
            val = str(val)
            val = val + "*"
        elif opt == "-":
            val = round(val1 - val2,5)
            val = str(val)
            val = val + "*"
        elif opt == "*":
            val = round(val1 * val2,5)
            val = str(val)
            val = val + "*"
        elif opt == "/":
            val = round(val1 / val2, 5)
            val = str(val)
            val = val + "*"
        data.set(val)
    else:
        if val == "":
            val  = '0' + "*"
        else:
            val = val + '*'
        data.set(val)





# Minus Button Clicked
def operatorClickSubtraction():
    global val
    global previousVal
    global next
    opt = ""
    optPresent = False
    
    for i in range(0,len(val)):
        if val[i] == "+":
            optPresent = True
            previousVal = val.split("+")[0]
            next = val.split("+")[1]
            opt = "+"
            break
        elif val[i] == "-":
            optPresent = True
            previousVal = val.split("-")[0]
            next = val.split("-")[1]
            opt = "-"
            break
        elif val[i] == "*":
            optPresent = True
            previousVal = val.split("*")[0]
            next = val.split("*")[1]
            opt = "*"
            break
        elif val[i] == "/":
            optPresent = True
            previousVal = val.split("/")[0]
            next = val.split("/")[1]
            opt = "/"
            break

    if optPresent == True:
        val1 = float(previousVal)
        val2 = float(next)
        if opt == "+":
            val = round(val1 + val2,5)
            val = str(val)
            val = val + "-"
        elif opt == "-":
            val = round(val1 - val2,5)
            val = str(val)
            val = val + "-"
        elif opt == "*":
            val = round(val1 * val2,5)
            val = str(val)
            val = val + "-"
        elif opt == "/":
            val = round(val1 / val2, 5)
            val = str(val)
            val = val + "-"
        data.set(val)
    else:
        if val == "":
            val  = '0' + "-"
        else:
            val = val + '-'
        data.set(val)



# Plus Button Click
def operatorClickPlus():
    global val
    global previousVal
    global next
    opt = ""
    optPresent = False
    
    for i in range(0,len(val)):
        if val[i] == "+":
            optPresent = True
            previousVal = val.split("+")[0]
            next = val.split("+")[1]
            opt = "+"
            break
        elif val[i] == "-":
            optPresent = True
            previousVal = val.split("-")[0]
            next = val.split("-")[1]
            opt = "-"
            break
        elif val[i] == "*":
            optPresent = True
            previousVal = val.split("*")[0]
            next = val.split("*")[1]
            opt = "*"
            break
        elif val[i] == "/":
            optPresent = True
            previousVal = val.split("/")[0]
            next = val.split("/")[1]
            opt = "/"
            break

    if optPresent == True:
        val1 = float(previousVal)
        val2 = float(next)
        if opt == "+":
            val = round(val1 + val2,5)
            val = str(val)
            val = val + "+"
        elif opt == "-":
            val = round(val1 - val2,5)
            val = str(val)
            val = val + "+"
        elif opt == "*":
            val = round(val1 * val2,5)
            val = str(val)
            val = val + "+"
        elif opt == "/":
            val = round(val1 / val2,5)
            val = str(val)
            val = val + "+"
        data.set(val)
    else:
        if val == "":
            val  = '0' + "+"
        else:
            val = val + '+'
        data.set(val)


def generateResult():
    global previousVal
    global next
    global val
    result = 0

    for i in range(0, len(val)):
        if val[i] == "+":
            previousVal = val.split("+")[0]
            next = val.split("+")[1]
            result = round(float(previousVal) + float(next),5)
            break
        elif val[i] == "-":
            previousVal = val.split("-")[0]
            next = val.split("-")[1]
            result = round(float(previousVal) - float(next),5)
            break
        elif val[i] == "*":
            previousVal = val.split("*")[0]
            next = val.split("*")[1]
            result = round(float(previousVal) * float(next),5)
            break
        elif val[i] == "/":
            previousVal = val.split("/")[0]
            next = val.split("/")[1]
            if previousVal == "0":
                result = 'Error'
                break
            else:
                result = round(float(previousVal) / float(next),5)
                break
        else:
            data.set(val)
    val = str(result)
    data.set(val)







# clear btn frame

clear = Frame(root)
clear.pack(expand = True, fill = 'both')



clearBtn = Button(
    clear,
    bg = '#88fce1',
    text = "CE",
    font = ("Vernada", 22),
    relief = GROOVE,
    command = btnclickClear,
    border = 0
    )
clearBtn.pack(side = LEFT, expand = True , fill = 'both')
back = Button(
    clear,
    bg = '#88fce1',
    text = "BS",
    font = ("Vernada", 22),
    relief = GROOVE,
    command = btnclickBack,
    border = 0
)
back.pack(side = LEFT, expand = True , fill = 'both')

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
    command = btnclickPoint,
    border = 0
)
pointBtn.pack(side = LEFT, expand = True , fill = 'both')

zeroBtn = Button(
    btnRow4,
    text = "0",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = btnclick0
)
zeroBtn.pack(side = LEFT, expand = True , fill = 'both')

equalBtn = Button(
    btnRow4,
    text = "=",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = generateResult
)
equalBtn.pack(side = LEFT, expand = True , fill = 'both')

plusBtn = Button(
    btnRow4,
    text = "+",
    font = ("Vernada", 22),
    relief = GROOVE,
    command = operatorClickPlus,
    border = 0
)
plusBtn.pack(side = LEFT, expand = True , fill = 'both')

# 3rd BTN ROW
btn1st = Button(
    btnRow3,
    text = "1",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = btnclick1
)
btn1st.pack(side = LEFT, expand = True , fill = 'both')

btn2nd = Button(
    btnRow3,
    text = "2",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = btnclick2
)
btn2nd.pack(side = LEFT, expand = True , fill = 'both')

btn3rd = Button(
    btnRow3,
    text = "3",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = btnclick3
)
btn3rd.pack(side = LEFT, expand = True , fill = 'both')

subtractionBtn = Button(
    btnRow3,
    text = "-",
    font = ("Vernada", 22),
    relief = GROOVE,
    command = operatorClickSubtraction,
    border = 0
)
subtractionBtn.pack(side = LEFT, expand = True , fill = 'both')

# 2nd BTN ROW
btn4th = Button(
    btnRow2,
    text = "4",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = btnclick4
)
btn4th.pack(side = LEFT, expand = True , fill = 'both')

btn5th = Button(
    btnRow2,
    text = "5",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = btnclick5
)
btn5th.pack(side = LEFT, expand = True , fill = 'both')

btn6th = Button(
    btnRow2,
    text = "6",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = btnclick6
)
btn6th.pack(side = LEFT, expand = True , fill = 'both')

multipleBtn = Button(
    btnRow2,
    text = "*",
    font = ("Vernada", 22),
    relief = GROOVE,
    command = operatorClickMultiplication,
    border = 0
)
multipleBtn.pack(side = LEFT, expand = True , fill = 'both')

# 2nd BTN ROW
btn7th = Button(
    btnRow1,
    text = "7",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = btnclick7
)
btn7th.pack(side = LEFT, expand = True , fill = 'both')

btn8th = Button(
    btnRow1,
    text = "8",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = btnclick8
)
btn8th.pack(side = LEFT, expand = True , fill = 'both')

btn9th = Button(
    btnRow1,
    text = "9",
    font = ("Vernada", 22),
    relief = GROOVE,
    border = 0,
    command = btnclick9
)
btn9th.pack(side = LEFT, expand = True , fill = 'both')

divisionBtn = Button(
    btnRow1,
    text = "/",
    font = ("Vernada", 22),
    relief = GROOVE,
    command = operatorClickDivision,
    border = 0
)
divisionBtn.pack(side = LEFT, expand = True , fill = 'both')


root.mainloop()
