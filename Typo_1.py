from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.title("Typo")
#root.iconbitmap("key.ico")
root.geometry("400x400")

import time
NF = open("MyText.txt",'r')


NewFile = NF.read()

L1 = Label(root, text=NewFile, anchor='center', bd=10).grid(row=0, column=0, columnspan=3)
NF.close()


def start(data):
    global Cs
    Cs = Entry(root)
    Cs.grid(row=1, column=1)
    global t1
    t1 = time.time()


def submit(data):
    word=1
    c=0
    c1=0
    t2 = time.time() - t1
    new = str(Cs.get())
    for i in range(len(new)):
        c1=c1+1
        if new[i]==" ":
            word=word+1
        if new[i]==NewFile[i]:
            c=c+1
    global L2, L3, L4   
    if c1==0:
        L2 = Label(root, text="Empty").grid(row=4, column=2)
    else:
        L2 = Label(root, text="Accuracy:"+str(round((c/c1)*100,3))+"%").grid(row=4, column=2)
        L3 = Label(root, text="Speed:"+ str(round(word*60/t2,3))+"wpm").grid(row=5, column=2)
        L4 = Label(root, text="Words:"+str(word)).grid(row=6, column=2)

B1 = Button(root, text="Start", bg="red", fg="white", command=lambda:start(1)).grid(row=1, column=0)
B2 = Button(root, text="Submit", bg="blue", fg="white", command=lambda:submit(2)).grid(row=1, column=2) 


def Edit():
    

    Pop = Toplevel(root)
    E2 = Entry(Pop, width=100)
    E2.grid(row=0, column=0)
    Text = open("MyText.txt",'a')

    def Save():
        Text.write(E2.get()+"\n")
        Text.close()
        Lay = mb.showinfo("Information", "Saved!")
        
        Pop.quit()


    
    B4 = Button(Pop,text='Save', command=Save).grid(row=1, column=0)

    Pop.mainloop()
    

B3 = Button(root, text ="Edit", bg="green", fg="white", command=Edit)
B3.grid(row=2, column=2)

root.mainloop()
