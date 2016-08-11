import tkinter
import VerbindungsAufbau


class MyGui(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # Eingabefelder
        # Eingabefeld IP
        self.ipEntry = tkinter.Entry(self)
        self.ipEntry.pack()
        self.ip = tkinter.StringVar()
        self.ip.set("127.0.0.1")
        self.ipEntry["textvariable"] = self.ip
        # Eingabefeld Port
        self.portEntry = tkinter.Entry(self)
        self.portEntry.pack()
        self.port = tkinter.StringVar()
        self.port.set("212")
        self.portEntry["textvariable"] = self.port
        # Buttons
        # Stop Button
        self.end = tkinter.Button(self)
        self.end["text"] = "Stop"
        self.end["command"] = self.quit
        self.end.pack(side="right")
        # Verbindungsbutton
        self.verbinden = tkinter.Button()
        self.verbinden["text"] = "Verbindungsaufbau"
        auf = lambda: VerbindungsAufbau.VerbindungsAufbau.aufbau(self.ip.get(), int(self.port.get()), "Hey", 5)
        self.verbinden["command"] = auf
        self.verbinden.pack(side="left")

    def starten():
        root = tkinter.Tk()
        app = MyGui(root)
        app.mainloop()
