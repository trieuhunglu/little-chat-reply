import socket
server = socket.socket()
server.bind(("localhost", 5555))
server.listen()

print("Server created")
print("Waiting for connection...")

client, address = server.accept()

print("Connected!")
print(address)

message = client.recv(1024)
print(message.decode())

reply = input("Reply: Dano bel ")
client.send(reply.encode())