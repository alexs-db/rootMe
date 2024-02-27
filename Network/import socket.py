import socket
import math
host= "challenge01.root-me.org"
port = 52002
# créer une connexion socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# laisser le client se connecter
client.connect((host, port))

# recevoir des données
response = client.recv(1024).decode()
print(response)


u1 = int(response.split(" ")[24])

u2 = int(response.split(" ")[28])

reponse = round(math.sqrt(u1) * u2,2)

fin = (str(reponse) + "\n").encode()

client.send(fin)

print(client.recv(1024).decode())