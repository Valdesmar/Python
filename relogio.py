import time 
from tkinter import*

root = Tk()
root.title('Relógio Digital')


def timer():
    string = time.strftime('%H:%M:%S %p')
    screen_text.config(text=string)
    screen_text.after(1000,timer)


screen_text = Label(font=('Times New Roman', 60, 'bold'))


screen_text.pack(anchor='center')
timer()

root.mainloop()
