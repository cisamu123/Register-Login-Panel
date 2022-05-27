from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
def click():
	username = username_entry.get()
	password = password_entry.get()

	messagebox.showinfo('Login successfully completed', f'{username}, {password}')
	noteopen1 = open('Saved.txt', 'a') 
	noteopen1.write("USER LOGIN TO ACCOUNT: ")
	noteopen1.write("Username: " + username) 
	noteopen1.write(" password: " + password)
	noteopen1.close()
window = Tk()
#WINDOW TITLE
window.title("GUI BY CISAMU")
#WINDOW GEOMETRY
window.geometry("400x500+600+300")
window.resizable(False, False)
#WINDOW ICO
window.iconbitmap("Icon.ico")
#WINDOW BACKGROUND
window['bg'] = 'black'
logintxt = Label(window, text='LOGIN', font='Arial 15 bold', bg='black', fg='white')
logintxt.pack()
username_label = Label(window, text='USERNAME', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
username_label.pack()
username_entry  = Entry(window, font='Arial 12', bg='black', fg='lime')
username_entry.pack()
password_label = Label(window, text='PASSWORD', font='Arial 11 bold', bg='black', fg='white', padx=10, pady=8)
password_label.pack()
password_entry  = Entry(window, font='Arial 12', bg='black', fg='lime')
password_entry.pack()

send_btn = Button(window, text='Login', command=click)
send_btn.pack(padx=10,pady=8)
window.mainloop()