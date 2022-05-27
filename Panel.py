from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import os
def start():
	print("Hello!")
	print("Made a small Register-Login Panel program. Use for any purpose, the program is open source. I ask you to mark the author under your modification. Because I have reserved all rights to use")
	print("#Author Cisamu")
	print("#All rights reserved (c)2022")
def login():
	file = 'Login.py'
	os.startfile(file)
def reg():
	file = 'Register.py'
	os.startfile(file)
window = Tk()
#WINDOW TITLE
window.title("REGISTER PANEL BY CISAMU")
#WINDOW GEOMETRY
window.geometry("400x500+600+300")
window.resizable(False, False)
#WINDOW ICO
window.iconbitmap("Icon.ico")
#WINDOW BACKGROUND
window['bg'] = 'black'
logintxt = Label(window, text='PANEL', font='Arial 15 bold', bg='black', fg='white')
logintxt.pack()
send_btn = Button(window, text='Login', command=login)
send_btn.pack(padx=10,pady=8)
send_btn = Button(window, text='Register', command=reg)
send_btn.pack(padx=10,pady=8)
window.mainloop()
#Author Cisamu
#All rights reserved (c)2022