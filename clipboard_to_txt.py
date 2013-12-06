from Tkinter import Tk
r = Tk()
r.withdraw()
txt = r.clipboard_get()
r.clipboard_clear()
r.clipboard_append(txt)
r.destroy()


