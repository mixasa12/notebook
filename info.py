from tkinter import *
def click1():
    global flagVisible
    def on_closing():
        global flagVisible
        flagVisible = False
        form2.destroy()
    if flagVisible: return 0
    flagVisible = True
    form2 = Toplevel()
    btn = Button(form2,text="Закрыть", command=on_closing).place(x=275, y=115)
    labelModal = Label(form2,justify=LEFT, text="Приложение с графическим интерфейсом \n «Блокнот ТСО» (файл приложения: ТСО). \n Позволяет: создавать / открывать / сохранять \n зашифрованный тестовый файл, предусмотрены \n ввод и сохранение личного ключа, \n вывод не модальной формы «Справка», \n вывод модальной формы «О программе».").place(x=5, y=5)
    form2.title("f2")
    form2.geometry("350x150")
    form2.protocol("WM_DELETE_WINDOW", on_closing)

def click2():
    formModal = Toplevel()
    formModal.geometry("280x100")
    btn = Button(formModal,text="Ок",width=5, compound="c",command=formModal.destroy).place(x=230, y=60)
    labelModal = Label(formModal, text="Программа для ‘прозрачного шифрования`\n(©) Тмуко О... Виза, 2029.").place(x=5, y=5)
    formModal.focus()
    formModal.grab_set()

flagVisible=False
