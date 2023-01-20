from tkinter import *

window = Tk()
window.title("Simple Interest Calculator")
window.geometry("400x500")
window.configure(bg="grey")

def  calculateSI():
    p=float(p_.get())
    r=float(r_.get())
    t=float(t_.get())
    si=(p*r*t)/100
    interest=round(si,2)
    result.destroy()
    
    message=Label(result_frame,text="Interest is Rs."+str(interest), bg = "grey", font=("Calibri", 12), width=55)
    message.place(x=20,y=40)
    message.pack()


app_label = Label(window,text="Simple Interest calculator", fg="black", bg="grey", font=("Calibri",30), bd=4)
app_label.place(x=50,y=20)

p_label = Label(window,text="Principal: ", fg="black", bg="grey", font=("Calibri",15), bd=4)
p_label.place(x=20,y=100)
p_=Entry(window,text="", width=40,bd=2)
p_.place(x=110,y=108)

r_label = Label(window,text="Rate(%): ", fg="black", bg="grey", font=("Calibri",15), bd=4)
r_label.place(x=20,y=160)
r_=Entry(window,text="", width=40,bd=2)
r_.place(x=110,y=168)

t_label = Label(window,text="Time(yrs): ", fg="black", bg="grey", font=("Calibri",15), bd=4)
t_label.place(x=20,y=220)
t_=Entry(window,text="", width=40,bd=2)
t_.place(x=110,y=228)

calculate_button = Button(window,text="Calculate",fg="black",bg="white",bd=2,command=calculateSI)
calculate_button.place(x=150,y=290)


result_frame = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 15))
result_frame.pack(padx=40, pady=10)
result_frame.place(x=20,y=320)

result=Label(result_frame,text="", bg = "grey", font=("Calibri", 12), width=55)
result.place(x=20,y=20)
result.pack()

window.mainloop()