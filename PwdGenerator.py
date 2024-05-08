from tkinter import*
import random, string
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Password Generator using python")
Label(root,text="PASSWORD GENERATOR",font='arial 12 bold').pack()
Label(root,text='Python',font='arial 12 bold').pack(side=BOTTOM)

pass_label = Label(root,text='Password length',font='arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root,from_=8,to_=32,textvariable=pass_label,width=15).pack()

pass_str = StringVar()
def Generator():
    password = ""
    for x in range(0,4):
        password = random.choice(string.ascii_uppercase)+ random.choice(string.ascii_lowercase)+ random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()-4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase+string.digits+string.punctuation)
    pass_str.set(password)

Button(root,text="Generate Password",command=Generator).pack(pady=5)
Entry(root,textvariable=pass_str).pack()

def Copy_pwd():
    pyperclip.copy(pass_str.get())
    Button(root,text='Copy to Clipboard',command=Copy_pwd).pack(pady=5)

root.mainloop()
