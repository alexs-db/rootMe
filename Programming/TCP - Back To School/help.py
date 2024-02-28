import socket
import math
host= "challenge01.root-me.org"
port = 52002



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))


response = client.recv(1024).decode()
print(response)