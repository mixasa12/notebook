from tkinter import *
import info
from info import click1
from info import click2
import actionwithfiles as files
from actionwithfiles import new
from actionwithfiles import open_file
from actionwithfiles import save
from actionwithfiles import save_as
from tkinter import messagebox
from tkinter import messagebox as ms
from tkinter import filedialog as fd
import changekey as ck
from changekey import parametr



    
mainForm = Tk()
mainForm.title("AmTCD")
mainForm.geometry("720x480")
mainForm.my_key=1
mainForm.another_key=1
main_menu = Menu()

file_menu = Menu(tearoff=0)
file_menu.add_command(label="Новый",command=lambda:files.new(txt,mainForm.my_key))
file_menu.add_command(label="Открыть",command=lambda:files.open_file(txt,mainForm.my_key))
file_menu.add_command(label="Сохранить",command=lambda:files.save(txt,mainForm.my_key))
file_menu.add_command(label="Сохранить как...",command=lambda:files.save_as(txt,mainForm.my_key))
file_menu.add_separator()
file_menu.add_command(label="Выход",command=mainForm.destroy)
main_menu.add_cascade(label="Файл", menu=file_menu)

edit_menu = Menu(tearoff=0)
edit_menu.add_command(label="Копировать",command=lambda: txt.event_generate("<<Copy>>"))
edit_menu.add_command(label="Вставить",command=lambda: txt.event_generate("<<Paste>>"))
edit_menu.add_separator()
edit_menu.add_command(label="Параметры",command=lambda:ck.parametr(mainForm))
main_menu.add_cascade(label="Правка", menu=edit_menu)

help_menu = Menu(tearoff=0)
help_menu.add_command(label="Содержание", command=info.click1)
help_menu.add_separator()
help_menu.add_command(label="О программе", command=info.click2)
main_menu.add_cascade(label="Справка", menu=help_menu)

mainForm.config(menu=main_menu)

scroll = Scrollbar(mainForm)
scroll.pack(side=RIGHT, fill=Y)

txt = Text(height=480, width=720, fg='black', yscrollcommand=scroll.set)
txt.pack(side=LEFT)

scroll.config(command=txt.yview)

mainForm.mainloop() 
