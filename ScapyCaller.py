from scapy.all import IP,send,TCP

def createPacket(werte):
    if not werte[0]:
        print("Geben Sie bitte eine IP ein")
    else:
        packet = IP(dst=werte[0]) / TCP()
    if not werte[1]:
        print("Gib Port ein")
    else:
        packet.dport = int(werte[1])
        send(packet)
    if werte[2]:
        packet.sport = int(werte[2])
        