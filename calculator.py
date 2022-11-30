from tkinter import *

app=Tk()
app.geometry("400x400")
app.title("calculator by nikki")

expression = ""

displayText = StringVar()

def press(num):
    global expression
    expression += num
    displayText.set(expression)
    
def equal():
        global expression
        total = eval(expression)
        displayText.set(total)
def clearDisplay():
    global expression
    expression = ""
    displayText.set("0")
        
        
display= Entry(app,width=17,font=("Arial",24),textvariable=displayText)


btn1 = Button(app, text="1",padx=10, pady=10, font=("Arial",22),command=lambda: press("1"))
btn2= Button(app, text="2",padx=10, pady=10, font=("Arial",22),command=lambda: press("2"))
btn3 = Button(app, text="3",padx=10, pady=10, font=("Arial",22),command=lambda: press("3"))
btn4 = Button(app, text="+",padx=10, pady=10, font=("Arial",22),command=lambda: press("+"))

btn5 = Button(app, text="4",padx=10, pady=10, font=("Arial",22),command=lambda: press("4"))
btn6 = Button(app, text="5",padx=10, pady=10, font=("Arial",22),command=lambda: press("5"))
btn7 = Button(app, text="6",padx=10, pady=10, font=("Arial",22),command=lambda: press("6"))
btn8 = Button(app, text="-",padx=10, pady=10, font=("Arial",22),command=lambda: press("-"))

btn9= Button(app, text="7",padx=10, pady=10, font=("Arial",22),command=lambda: press("7"))
btn10= Button(app, text="8",padx=10, pady=10, font=("Arial",22),command=lambda: press("8"))
btn11= Button(app, text="9",padx=10, pady=10, font=("Arial",22),command=lambda: press("9"))
btn12= Button(app, text="/",padx=10, pady=10, font=("Arial",22),command=lambda: press("/"))

btn13= Button(app, text="0",padx=10, pady=10, font=("Arial",22),command=lambda: press("0"))
btn14= Button(app, text="=",padx=10, pady=10, font=("Arial",22), command=equal)
btn15= Button(app, text="C",padx=10, pady=10, font=("Arial",22),bg="red",fg="white",command=clearDisplay)
btn16 = Button(app, text="x",padx=10, pady=10, font=("Arial",22),command=lambda: press("*"))

display.grid(row=0, column=0,columnspan=4,padx=10, pady=10)

btn1.grid(row=1, column=0, padx=10, pady=10)
btn2.grid(row=1, column=1, padx=10, pady=10)
btn3.grid(row=1, column=2, padx=10, pady=10)
btn4.grid(row=1, column=3, padx=10, pady=10)

btn5.grid(row=2, column=0, padx=10, pady=10)
btn6.grid(row=2, column=1, padx=10, pady=10)
btn7.grid(row=2, column=2, padx=10, pady=10)
btn8.grid(row=2, column=3, padx=10, pady=10)

btn9.grid(row=3, column=0, padx=10, pady=10)
btn10.grid(row=3, column=1, padx=10, pady=10)
btn11.grid(row=3, column=2, padx=10, pady=10)
btn12.grid(row=3, column=3, padx=10, pady=10)

btn13.grid(row=4, column=0, padx=10, pady=10)
btn14.grid(row=4, column=1, padx=10, pady=10)
btn15.grid(row=4, column=2, padx=10, pady=10)
btn16.grid(row=4, column=3, padx=10, pady=10)
app.mainloop()