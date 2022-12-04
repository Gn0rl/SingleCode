from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as msg
import platform
import sys
import os
import subprocess

ide = Tk()
name = 'SingleCode'
ide.title(f'untitled - {name}')
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def save():
    pass

def save_as():
    if file_path == '':
        path = asksaveasfile(filetypes=[('SingleScript files', '*.sin')])
        print(path.name)
    else:
        path = file_path
    with open(path.name, "w") as file:
        code = editor.get('1.0',END)
        file.write(code)
        set_file_path(path)
        ide.title(f"{path.name} - {name}")

# def run():
#     if file_path == '':
#         msg.showwarning('File is dont saved', 'Please save you file')
#     else:
#         command = f'idk'
#         save_as()
#         procces = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess,shell=True)
#         output,error = procces.communicate()
#         code_output.config(state='normal')
#         code_output.insert('1.0',output)
#         code_output.insert('1.0',error)
#         code_output.config(state='disabled')
        

def open_file():
    path = askopenfile(filetypes=[('SingleScript files', '*.sin')])
    try:
        with open(path.name,"r") as file:
            code = file.read()
            editor.delete('1.0',END)
            editor.insert('1.0',code)
            ide.title(f"{path.name} - {name}")
    except:
        print('error')

def update_label():
    row,col = editor.index('insert').split('.')
    label.config(text=f'SingleScript:None Line:{row} Column:{col}')
    ide.after(100,update_label)

editor = ScrolledText(undo=True)
editor.pack()

menubar = Menu(ide)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label='Open',command=open_file)
filemenu.add_command(label='Save',command=save_as)
filemenu.add_command(label='Exit',command=quit)

menubar.add_cascade(label='File',menu=filemenu)


ide.config(menu=menubar)

code_output = ScrolledText(height=10,state='disabled')
code_output.pack()

label = Label(ide, anchor='e')
label.pack(fill='x')

update_label()

if __name__ == '__main__':
    ide.mainloop()