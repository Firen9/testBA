from scapy.all import IP,send,TCP,sr1
import MyGui
from Tkinter import *

def createPacket(werte):
    if not werte[0]:
        print("Geben Sie bitte eine IP ein")
    else:
        packet = IP(dst=werte[0]) / TCP()
        ip = True
    if not werte[1]:
        print("Gib Port ein")
    else:
        packet.dport = int(werte[1])
        port = True
    if werte[2]:
        packet.sport = int(werte[2])
    if werte[3]:
        packet.ack = int(werte[3])
    if werte[4]:
        packet.dataofs = int(werte[4])
    if werte[5]:
        packet.reserved = int(werte[5])
    if werte[6]:
        packet.flags = int(werte[6])
    if werte[7]:
        packet.urgptr = int(werte[7])
    if werte[8]:
        packet.options = werte[8]
    if ip and port:
        antwort=sr1(packet)
        answerWindow(antwort.show())
    else:
        print("IP oder Port eingeben")

def answerWindow(antwortPacket):
    answer = MyGui.Toplevel()
    msg = Message(answer, text=antwortPacket)
    msg.pack()