from tkinter import *
import tkinter as tk

import configMod as cm
from configMod import set_public_key
from configMod import get_public_key

def parametr(form):
    path="main.ini"
    formSettings = Toplevel()
    formSettings.geometry("600x210")
    formSettings.title("Параметры")
    def rk():
        if str(entry_my_key.get()).isdigit():
            if int(str(entry_my_key.get()))>0:
                form.my_key=int(str(entry_my_key.get()))
                label_my_key["text"]="Ваш ключ: " + str(entry_my_key.get())
                cm.set_public_key(path,str(form.my_key*form.another_key))
    def ark():
        if str(entry_friend_key.get()).isdigit():
            if int(str(entry_friend_key.get()))>0:
                form.another_key=int(str(entry_friend_key.get()))
                label_friend_key["text"]="Ключ собеседника: " + str(entry_friend_key.get())
                cm.set_public_key(path,str(form.my_key*form.another_key))

                
    entry_friend_key = tk.Entry(formSettings)
    entry_friend_key.grid(column = 1, row = 1,padx=20,pady=10)
    label_friend_key = Label(formSettings, text="Ключ собеседника: " + str(form.another_key))
    label_friend_key.grid(column = 2, row = 1,padx=30)
    btn_friend_read_key = Button(formSettings,text="Поменять",command=ark).place(x=500, y=10)
    entry_my_key = tk.Entry(formSettings)
    entry_my_key.grid(column = 1, row = 2,pady=56)
    label_my_key = Label(formSettings, text="Ваш ключ: " + str(form.my_key))
    label_my_key.grid(column = 2, row = 2)
    btn_my_write_key = Button(formSettings,text="Поменять",command=rk).place(x=500, y=100)
    btn_my_read_key = Button(formSettings,text="Выйти",command=formSettings.destroy).place(x=550, y=175)
    formSettings.focus()
    formSettings.grab_set()
