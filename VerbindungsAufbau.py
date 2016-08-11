import socket


# Klasse zum Verbingsaufbau und die dazu benötigten methode
class VerbindungsAufbau():
    def aufbau(ip, port, nachricht, anzahl):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((ip,port))
            for i in range(anzahl):
                s.send((nachricht+"\n").encode())
