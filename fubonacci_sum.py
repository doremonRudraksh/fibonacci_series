from tkinter import *

root = Tk()

root.title("fibonacci")
root.geometry("400x400")
root.configure(background= "snow")



enter_word = Entry(root)
enter_word.place(relx=0.5, rely = 0.5, anchor=CENTER)

label = Label(root,text="name in fibonacci: ", bg="light yellow", fg="black")
label2 = Label(root,text="sum of fibonacci series,", bg="light yellow", fg="black")

def fibbonacci_generator():
    input_word = enter_word.get()

    for r in input_word:
        label2["text"]+=str(sum2) 

def fibbonacci_sum():
    num1=0
    num2=1
    sum=num1+num2
    sum2=0
    sum2 = sum2+sum

btn=Button(root, text="show fibonacci series", command=fibbonacci_sum, bg="gold", fg="black")
btn.place(relx=0.5, rely=0.6, anchor=CENTER)
label.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()


        




