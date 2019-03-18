#!/usr/bin/env python3
### reference: https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
# 1 - creating frame
# 2 - creating button
# 3 - event handling (button) with commands
# 4 - menus and submenus


from tkinter import *
from tkinter import filedialog
import pandas as pd



class Window(Frame):  # inhereting class frame (widget)
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()



    ### button event handling
    def client_exit(self):
        exit()

    def UploadAction(event=None):
        filename = filedialog.askopenfilename()
        print('Selected:', filename)
        df = pd.read_excel(filename)
        print('Data columns:', df.columns)

    ### create init_window, with menus
    def init_window(self):

        self.master.title("my GUI")
        self.pack(fill=BOTH, expand=1)  # allows widget to take full space of root window (frame)

        ### Menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Menu dropdown - "file"
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="MyFile", menu=file)

        # Menu dropdown - "edit"
        edit = Menu(menu)
        edit.add_command(label="Undo")
        # edit.add_command(label="Show Img", command=self.showImg)
        # edit.add_command(label="Show Text", command=self.showText)
        menu.add_cascade(label="myEdit", menu=edit)

        ### Buttons
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)  # place starts upper left

        uploadButton = Button(self, text='Open file', command=self.UploadAction)
        uploadButton.place(x=0, y=100)





root = Tk()
root.geometry("400x300")

# Create & Run Window
app = Window(root)
root.mainloop()


# todo: choose output destination / filename
# todo: display heading of data in window
# todo: size buttons/window relatively
# todo: graph data in window? numpy/matplotlib