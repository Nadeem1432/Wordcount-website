from tkinter import *
r = Tk()
x= r.withdraw()
print(x)
r.clipboard_clear()
r.clipboard_append('i can has clipboardz?')
r.destroy()
