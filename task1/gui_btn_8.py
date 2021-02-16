# 8. Write a program that displays a single button on a GUI window.
# When the button is clicked, it should print "I've been clicked x times" where 'x' is a counter for the number of times the button has been clicked

import tkinter as tk

count = 0


def print_count():
    global count
    count += 1
    print(f'I have been clicked {count} times.')


window = tk.Tk()
window.geometry('150x150')
frame = tk.Frame(window)
frame.pack()

button = tk.Button(text='Clickable',
                   command=print_count)
button.pack()

window.mainloop()
