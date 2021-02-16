# 7. Write a program that displays hello world on a GUI window


import tkinter as tk

window = tk.Tk()
window.geometry('150x150')
frame = tk.Frame(window)
frame.pack()

hello = tk.Label(text='Hello World!!!')
hello.pack()

window.mainloop()
