import socket
import math
host= "challenge01.root-me.org"
port = 52023
# créer une connexion socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# laisser le client se connecter
client.connect((host, port))

# recevoir des données
response = client.recv(1024).decode()

x = response.split(" ")[14]

x.encode("utf-8")

print(x)




