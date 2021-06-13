import tkinter as tk
import math
root=tk.Tk()
 
# setting the windows size
root.geometry("450x400")
root.title('Rectangular DRA Resonant Frequency Calculator')
# declaring string variable
permittivity=tk.StringVar()
permeability=tk.StringVar()
length = tk.StringVar()
width = tk.StringVar()
height = tk.StringVar()
  
# defining a function that will get the permittivity1 and permeability and print them on the screen
def submit():
 
    permittivity1=permittivity.get()
    permeability1=permeability.get()
    length1 = length.get()
    width1 = width.get()
    height1 = height.get()
    TE111_result = tk.Label(root,text='',font=('calibre',10, 'bold'))
    TE111_result.grid(row = 6,column =1)

    try:

        c = (3 * pow(10,8))/(math.sqrt(float(permittivity1)*float(permeability1))*2)
        a = round((1000/float(length1)),2)
        b = round((1000/float(width1)),2)
        d = round((1000/float(height1)),2)

        e,f,g = round(pow(a,2)),round(pow(b,2)),round(pow(d,2))
        
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
        final101 = round((dimen101*c)/pow(10,9),2)
        final011 = round((dimen011*c)/pow(10,9),2)
        final110 = round((dimen110*c)/pow(10,9),2)
        final010 = round((dimen010*c)/pow(10,9),2)
        final100 = round((dimen100*c)/pow(10,9),2)
        
        TE111_result.config(text='\n'+str(final111) + ' GHz in TE111 Mode\n' + str(final101) + ' GHz in TE101 Mode\n' + str(final011) + ' GHz in TE011 Mode\n' + str(final110) + ' GHz in TE110 Mode / TE11 Mode\n' + str(final010) + ' GHz in TE01 Mode\n' + str(final100) + ' GHz in TE10 Mode\n')

    except:
        global expression
        expression = "\n                      \n                                                     \n                     Error Try Again                    \n                                       \n"
        TE111_result.config(text=expression) #please don't interfere with the spaces (noob's trick)

# creating a label for permittivity1 using widget Label
permittivity_label = tk.Label(root, text = 'Permittivity', font=('calibre',10, 'bold'))
  
# creating a entry for input permittivity1 using widget Entry
permittivity_entry = tk.Entry(root,textvariable = permittivity, font=('calibre',10,'normal'),width = 50,borderwidth=5)
  
# creating a label for permeability
permeability_label = tk.Label(root, text = 'Permeability', font = ('calibre',10,'bold'))
  
# creating a entry for permeability
permeability_entry=tk.Entry(root, textvariable = permeability, font = ('calibre',10,'normal'),width = 50,borderwidth=5)

# creating a label for length using widget Label
length_label = tk.Label(root, text = 'length(mm)', font=('calibre',10, 'bold'))
  
# creating a entry for input length using widget Entry
length_entry = tk.Entry(root,textvariable = length, font=('calibre',10,'normal'),width = 50,borderwidth=5)

# creating a label for width using widget Label
width_label = tk.Label(root, text = 'width(mm)', font=('calibre',10, 'bold'))
  
# creating a entry for input width using widget Entry
width_entry = tk.Entry(root,textvariable = width, font=('calibre',10,'normal'),width = 50,borderwidth=5)

# creating a label for height using widget Label
height_label = tk.Label(root, text = 'height(mm)', font=('calibre',10, 'bold'))
  
# creating a entry for input height using widget Entry
height_entry = tk.Entry(root,textvariable = height, font=('calibre',10,'normal'),width = 50,borderwidth=5)
  
# creating a button using the widget Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)

text = tk.Label(root, text="Created by Yedhubooshan M M",font=('calibre',10, 'bold')).place(x=0,y=380)

def key_handler(event):
    if event.keysym in ("Return", "equal"):
        submit()

root.bind("<Key>", key_handler)



# placing the label and entry in the required position using grid method
permittivity_label.grid(row=0,column=0)
permittivity_entry.grid(row=0,column=1)
permeability_label.grid(row=1,column=0)
permeability_entry.grid(row=1,column=1)
length_label.grid(row=2,column=0)
length_entry.grid(row=2,column=1)
width_label.grid(row=3,column=0)
width_entry.grid(row=3,column=1)
height_label.grid(row=4,column=0)
height_entry.grid(row=4,column=1)
sub_btn.grid(row=5,column=1)

# performing an infinite loop for the window to display
root.mainloop()