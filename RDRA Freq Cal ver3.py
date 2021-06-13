import tkinter,math

def x(expression):
    #print(a,b,d)
    x = expression.split()
    c = (3 * pow(10,8))/(math.sqrt(float(x[0])*float(x[1]))*2)
    a = x[2]
    b = x[3]
    d = x[4]
    #print(a,b,d)
    a = round((1000/float(a)),2)
    b = round((1000/float(b)),2)
    d = round((1000/float(d)),2)

    e,f,g = round(pow(a,2)),round(pow(b,2)),round(pow(d,2))
    #print(e,f,g)

    total111 = (1*e) + (1*f) + (1*g)
    total101 = (1*e) + (0*f) + (1*g)
    total011 = (0*e) + (1*f) + (1*g)
    total110 = (1*e) + (1*f) + (0*g)
    total010 = (0*e) + (1*f) + (0*g)
    total100 = (1*e) + (0*f) + (0*g)


    dimen111 = math.sqrt(total111)
    dimen101 = math.sqrt(total101)
    dimen011 = math.sqrt(total011)
    dimen110 = math.sqrt(total110)
    dimen010 = math.sqrt(total010)
    dimen100 = math.sqrt(total100)


    final111 = round((dimen111*c)/pow(10,9),2)
    #print(str(final111) + ' GHz in TE111 Mode\n')

    final101 = round((dimen101*c)/pow(10,9),2)
    #print(str(final101) + ' GHz in TE101 Mode\n')

    final011 = round((dimen011*c)/pow(10,9),2)
    #print(str(final011) + ' GHz in TE011 Mode\n')

    final110 = round((dimen110*c)/pow(10,9),2)
    #print(str(final110) + ' GHz in TE110 Mode / TE11 Mode\n')

    final010 = round((dimen010*c)/pow(10,9),2)
    #print(str(final010) + ' GHz in TE01 Mode\n')

    final100 = round((dimen100*c)/pow(10,9),2)
    #print(str(final100) + ' GHz in TE10 Mode\n')
    
    return str(final111) + ' GHz in TE111 Mode\n' + str(final101) + ' GHz in TE101 Mode\n' + str(final011) + ' GHz in TE011 Mode\n' + str(final110) + ' GHz in TE110 Mode / TE11 Mode\n' + str(final010) + ' GHz in TE01 Mode\n' + str(final100) + ' GHz in TE10 Mode\n' , 'test'



root = tkinter.Tk()
root.title("RDRA Resonant Frequency Calculator")
#root.geometry("800x800")
expression = ""

# Create key bindings
def key_handler(event):
    global expression
    if event.keysym in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
        add(event.keysym)
    elif event.keysym == "plus":
        add("+")
    elif event.keysym == "space":
        add(" ")
    elif event.keysym in ("c", "C") or event.keysym == "Escape":
        clear()
    elif event.keysym == "period":
        add(".")
    elif event.keysym in ("Return", "equal"):
        calculate()
    elif event.keysym == "BackSpace":
        expression = expression[0:len(expression)-1]
        label_result.config(text=expression)
        
    
root.bind("<Key>", key_handler)
            
# Create GUI
label_result = tkinter.Label(root, text="Enter: (all units in mm)\n Order: Permittivity,Permeability,Length,Width,Height\n Press Space key button Between each dimension while giving input\n Press ESC or C for new calculation.\n\n Created by Yedhubooshan M M",height = 10,font=10, relief="solid",width=100)
label_result.grid(row=0, column=0, columnspan=4)

#label_result1 = tkinter.Label(root, text="Eg: 17,17,4",height = 2,font=10, relief="solid",width=100)
#label_result1.grid(row=1, column=0, columnspan=4)


# Create functions
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
    
def clear():
    global expression
    expression = ""
    #label_result.config(text=expression)
    label_result.config(text='Enter: (all units in mm)\n Order: Permittivity,Permeability,Length,Width,Height\n Press Space key button Between each dimension while giving input\n Press ESC or C for new calculation.\n\n Created by Yedhubooshan M M')
    
    

button_1 = tkinter.Button(root, text="1", command=lambda: add("1"),width = 25,borderwidth=5)
button_1.grid(row=2, column=0)

button_2 = tkinter.Button(root, text="2", command=lambda: add("2"),width = 25,borderwidth=5)
button_2.grid(row=2, column=1)

button_3 = tkinter.Button(root, text="3", command=lambda: add("3"),width = 25,borderwidth=5)
button_3.grid(row=2, column=2)

button_4 = tkinter.Button(root, text="4", command=lambda: add("4"),width = 25,borderwidth=5)
button_4.grid(row=3, column=0)

button_5 = tkinter.Button(root, text="5", command=lambda: add("5"),width = 25,borderwidth=5)
button_5.grid(row=3, column=1)

button_6 = tkinter.Button(root, text="6", command=lambda: add("6"),width = 25,borderwidth=5)
button_6.grid(row=3, column=2)

button_7 = tkinter.Button(root, text="7", command=lambda: add("7"),width = 25,borderwidth=5)
button_7.grid(row=4, column=0)

button_8 = tkinter.Button(root, text="8", command=lambda: add("8"),width = 25,borderwidth=5)
button_8.grid(row=4, column=1)

button_9 = tkinter.Button(root, text="9", command=lambda: add("9"),width = 25,borderwidth=5)
button_9.grid(row=4, column=2)

button_clear = tkinter.Button(root, text="C", command=lambda: clear(),width = 25,borderwidth=5)
button_clear.grid(row=5, column=0)

button_0 = tkinter.Button(root, text="0", command=lambda: add("0"),width = 25,borderwidth=5)
button_0.grid(row=5, column=1)

button_dot = tkinter.Button(root, text=".", command=lambda: add("."),width = 25,borderwidth=5)
button_dot.grid(row=5, column=2)

button_add = tkinter.Button(root, text="Space", command=lambda: add(" "),width = 30,height = 10,borderwidth=5)
button_add.grid(row=2, column=3,rowspan = 4)

def calculate():
    global expression
    result1,result2 = "",''
    if expression != "":
        try:
            result1,result2 = x(expression)
            result1+='\nPress ESC or C for new calculation.'
        except:
            result1,result2 = "error: Press ESC to Try again",""
            expression = ""
    label_result.config(text=result1)
    #label_result1.config(text=result2)

button_equals = tkinter.Button(root, text="Submit For Calculation", width=50, command=lambda: calculate(),borderwidth=5,font='50')
button_equals.grid(row=6, column=0, columnspan=4)

root.mainloop()