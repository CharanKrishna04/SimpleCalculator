from tkinter import *
import math
#taking an operator/expression
operator=""
#method to update information
#making expression global
def getandreplace(self): 
  
        """replace x with * and ÷ with /"""
        self.expression = self.e.get() 
        self.newtext=self.expression.replace('/','/') 
        self.newtext=self.newtext.replace('x','*') 
def click(n):
    global operator
    operator=operator+str(n)
    value.set(operator)
#evaluation
#exception handling
def dclick():
    try:
        global operator
        total=str(eval(operator))
        value.set(total)
        operator=""
    except:
        value.set("Error:Operation not possible.")
        operator=""
#method to clear previous contents to start new operation
def clear():
    global operator 
    operator = "" 
    value.set("") 
#now creating a customized GUI window
if __name__=="__main__":
    gui=Tk()#tkinter toolkit object
    gui.configure(background="light blue")
    gui.title("Calculator")
    gui.geometry("265x130")#size of the window
    value=StringVar()
    operator_area = Entry(gui, textvariable=value) 
    operator_area.grid(columnspan=4, ipadx=70)
    value.set('Enter your expression:')
#buttons customization
    
    button1 = Button(gui, text=' 1 ', fg='black', bg='grey',command=lambda: click(1), height=2, width=6) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='grey',command=lambda: click(2), height=2, width=6) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='grey',command=lambda: click(3), height=2, width=6) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='grey',command=lambda: click(4), height=2, width=6) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='grey',command=lambda: click(5), height=2, width=6) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='grey',command=lambda: click(6), height=2, width=6) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='grey',command=lambda: click(7), height=2, width=6) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='grey',command=lambda: click(8), height=2, width=6) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='grey',command=lambda: click(9), height=2, width=6) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='grey',command=lambda: click(0), height=2, width=6) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ', fg='black', bg='grey',command=lambda: click("+"), height=2, width=6) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', fg='black', bg='grey', command=lambda: click("-"), height=2, width=6) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' * ', fg='black', bg='grey', command=lambda: click("*"), height=2, width=6) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text=' / ', fg='black', bg='grey',command=lambda: click("/"), height=2, width=6) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', fg='black', bg='grey',command=dclick, height=2, width=6) 
    equal.grid(row=5, column=2) 
  
    clear = Button(gui, text='C', fg='black', bg='grey',command=clear, height=2, width=6)
    clear.grid(row=5, column='1')

    # start the GUI 
    gui.mainloop() 


