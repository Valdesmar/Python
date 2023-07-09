import time 
from tkinter import*

root = Tk()
# root.title('Relógio Digital')
# root.iconbitmap('iconeclock.ico')

root.overrideredirect(True)


def timer():
    string = time.strftime('%H:%M:%S %p')
    screen_text.config(text=string)
    screen_text.after(1000,timer)


def move_window(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


# Create a customized title bar
title_bar = Frame(root, bg='#424F64', relief='raised', border=1)
title_bar.pack(expand=1, fill=X)
title_bar.bind('<B1-Motion>', move_window)

# Add text to the titlebar
title_label = Label(title_bar, 
                    text='Relógio Digital', 
                    background='#424F64', 
                    foreground='white')
title_label.pack(side=LEFT, pady=2)


# Create a Button to close the window
quit_button = Button(title_bar, 
                     text='QUIT',
                     bg='#424F64',
                     fg='white',
                     relief='flat',
                     command=root.quit)
quit_button.pack(side=RIGHT, pady=2, padx=2)


# Time Text
screen_text = Label(font=('terminal', 60, 'bold'),
                    background='black', 
                    foreground='white')
screen_text.pack(anchor='center')


timer()
root.mainloop()
