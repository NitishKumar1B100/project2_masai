from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar # import the calender
root = Tk()
root.title('Calender Project')
root.geometry('600x400') # give the presenting size of window
style = Style(root) # this stye module for style buttons


c = Calendar() # create the calender 
turn = True
label = Label(root,text='Date: MM/DD/YY',
              font=('Arial',15,'bold'),foreground='#1e2d59') # this label(Label) store the date

def get_date():
    res = 'Date: '+str(c.get_date()) # convert inn string given date and date formate
    label.configure(text=res) # here set string date value
def show():
    global turn # Now make the glabal for access
    if(turn):
        turn = False
        c.grid(column=3) # display the Calender
        getDate.grid(column=4,row=5) # Display the getDate Button
        label.grid(column=3) # Display the label 'Label' 
    else:
        turn = True
        c.grid_forget() # Hide the Calender from main root
        getDate.grid_forget() # Hide the gerDate 'Button'
        label.configure(text='Date: MM/DD/YY') # Reset the Value
        label.grid_forget()# Hide the 'Label'


style.configure('TButton',font=('Arial',14),width=14,foreground='#0051FF') # Now I set the some style in Buttons
style.map('TButton',foreground=[('active','#4681f4')],background=[('active','#5783db')]) # Now Set the some hover style , it occure when mouse over on button

getDate = Button(root,text='date',command=get_date) # create the button that show the  calender
getCalender = Button(root,text='calender',command=show).grid() # create the button that display the selected date 
root.mainloop() # Last run this intire root