import socket


# Klasse zum Verbingsaufbau und die dazu benötigten methode
class VerbindungsAufbau():
    def aufbau(ip, port, nachricht, anzahl):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        try:
            i = 0
            while i <= anzahl:
                s.send(nachricht.encode())
                i += 1
        finally:
            s.close()
