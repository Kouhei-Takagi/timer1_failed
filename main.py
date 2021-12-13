from time import sleep
import tkinter
from tkinter import messagebox
from tkinter.constants import X
from typing import Text
import threading

target_time = 5

window = tkinter.Tk()
window.geometry('300x300')
window.title('Timer 5 minutes')

sv = tkinter.StringVar()
sv.set("0")

def btn_click():
    change_value_callback()
    looping()
    messagebox.showinfo("End", "5 minutes passed!")

def change_value_callback():
    thread1 = threading.Thread(target=change_value, args=())
    thread1.start()

def change_value(num1):
    print(num1)
    sv.set(num1)

def looping():
    for i in range(target_time):
        sleep(1)
        change_value(num1=i)
        print(i)

btn = tkinter.Button(text='Timer', command=btn_click)
btn.place(x=130, y=50)

word = tkinter.Label(textvariable=f"{sv}")
word.place(x=130, y=100)

window.mainloop()