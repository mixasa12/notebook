from tkinter import *

def er_of_key():
    formModal = Toplevel()
    formModal.geometry("280x80")
    btn = Button(formModal,text="Ок",width=5, compound="c",command=formModal.destroy).place(x=230, y=50)
    labelModal = Label(formModal, text="Неправильный ключ шифрования").place(x=5, y=5)
    formModal.focus()
    formModal.grab_set()
