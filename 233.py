from tkinter import *
window = Tk()

window.title('233')
window.geometry("500x500")

lbl = Label(window, text="2333333333333", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

btn = Entry(window,width=20)
btn.grid(column=0,row=5)
window.mainloop()
