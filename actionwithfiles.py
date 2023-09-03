from tkinter import *
from tkinter import messagebox
from tkinter import messagebox as ms
from tkinter import filedialog as fd
import code
from code import codeText
from code import uncodeText

def new(txt,m_k):
    global savefile
    if(str(txt.get(1.0,END)).isspace()):
        res=False
    else:
        res = ms.askyesno('Создание нового документа...','Сохранить предыдущий документ?')
    if res == True:
        save(txt,m_k)#вызов вункции сохранить( save )
        txt.delete('1.0', END)#удаление символов из документа
        savefile = None#обнуление пути сохранения
    elif res == False:
        txt.delete('1.0', END)#удаление символов из документа
        savefile = None#обнуление пути сохранения
    else:
        pass
        
def open_file(txt,m_k):
    global savefile
    if(str(txt.get(1.0,END)).isspace()):
        res=False
    else:
        res = ms.askyesno('Открытие документа...','Сохранить предыдущий документ?')
    if res == True:
        save(txt,m_k)
    fileopen = fd.askopenfilename(title="Select file",
                                        filetypes=(("txtx files", "*.txtx"), ("all files", "*.*")))
    if fileopen:
        file = open(fileopen, 'r', encoding="utf-8")
        data = file.read()
        data=code.uncodeText(data,m_k)
        txt.delete('1.0', END)
        txt.insert(END, data)
        savefile = fileopen

        
def save_as(txt,m_k):
    global savefile
    global text
    savefile = fd.asksaveasfilename(title="Select file",
                                            filetypes=(("txtx files", "*.txtx"), ("all files", "*.*"))) + ".txtx"#получение пути сохраниния
    if savefile:
        file = open(savefile, 'w', encoding="utf-8")#сохранение
        data = txt.get('1.0', END)
        data=code.codeText(data,m_k)
        file.write(data)#редактировать и записать

    
def save(txt,m_k):
    global savefile
    global text
    if savefile == None:#если пути нет то сохранение файла с укозанием пути
        save_as(txt,m_k)      
    else:#если путь есть то сохранение файла по данному пути
        file = open(savefile, 'w', encoding="utf-8")
        data = txt.get('1.0', END)
        data=code.codeText(data,m_k)
        file.write(data)

savefile=None
