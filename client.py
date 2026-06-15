import socket

client = socket.socket()

client.connect(("localhost", 5555))

print("Connected to server!")

message = input("Dano dau kiem 3ku: ")
client.send(message.encode())
reply = client.recv(1024)
print(reply.decode())