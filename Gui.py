import tkinter
import VerbindungsAufbau


class MyGui(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # Eingabefelder
        self.ipEntry = tkinter.Entry(self)
        self.portEntry = tkinter.Entry(self)
        self.ipEntry.pack()
        self.portEntry.pack()
        self.ip = tkinter.StringVar()
        self.ip.set("127.0.0.1")
        self.ipEntry["textvariable"] = self.ip
        self.port = tkinter.StringVar()
        self.port.set("21")
        self.portEntry["textvariable"] = self.port
        # Buttons
        self.end = tkinter.Button(self)
        self.end["text"] = "Stop"
        self.end["command"] = self.quit
        self.end.pack(side="right")
        self.verbinden = tkinter.Button()
        self.verbinden["text"] = "Verbindungsaufbau"
        intPort =int(self.port.get())
        auf = lambda: VerbindungsAufbau.VerbindungsAufbau.aufbau(self.ip.get(),intPort, "Hey", 5)
        self.verbinden["command"] = auf
        self.verbinden.pack(side="left")


root = tkinter.Tk()
app = MyGui(root)
app.mainloop()
