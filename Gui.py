import tkinter


class MyGui(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.ipEntry = tkinter.Entry(self)
        self.portEntry = tkinter.Entry(self)
        self.ipEntry.pack()
        self.portEntry.pack()