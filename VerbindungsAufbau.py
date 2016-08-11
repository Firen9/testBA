import socket


# Klasse zum Verbingsaufbau und die dazu benötigten methode
class VerbindungsAufbau():
    def aufbau(ip, port, nachricht, anzahl):
      try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((ip,port))
            for i in range(anzahl):
                s.send((nachricht+"\n").encode())
      except ConnectionRefusedError:
          print("Leider konnte keine Verbindung hergsetellt werden. \nBitte Überprüfen Sie ob die IP und der Port richtig sind")