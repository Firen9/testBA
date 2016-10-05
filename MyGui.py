from Tkinter import *
from scapy.all import IP,send,TCP

fields = 'IP', 'DPort', 'SPort', 'ACK', 'dataofs', 'reserved', 'flags', 'window', 'urggptr', 'options'

def fetch(entries):
   eingabe=[]

   for entry in entries:
      eingabe.append(entry[1].get())
     # print(entry[1].get())

   if not eingabe[0]:
      print("Geben Sie bitte eine IP ein")
   else:
      packet = IP(dst=eingabe[0])/TCP()
   if not eingabe[1]:
      print("Gib Port ein")
   else:
      packet.dport=int(eingabe[1])
      send(packet)




def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Verbinden', command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)

   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
