from tkinter import *
from tkinter.messagebox import showinfo
root = Tk()


def btn_click():
    login = loginInput.get()
    password = passField.get()

    info_str = f'Данные: {str(login)}, {str(password)}'
    showinfo(title='яляля', message=info_str)


root['bg'] = "#fefefe"
root.title('123')
# root.wm_attributes('-alpha', 0.7)
root.geometry('400x300')

root.resizable(width=False, height=False)

canvas = Canvas(root,height=400, width=300)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relx=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='эаэаээ', font=80)
title.pack()

btn = Button(frame, text='Я крутая кнопка', bg="gray", command=btn_click)
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

passField = Entry(frame, bg='white', show='*')
passField.pack()

root.mainloop()
