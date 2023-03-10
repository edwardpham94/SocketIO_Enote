import socket


# AF_INET = IP, SOCK_STREAM = TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1002))  # 127.0.0.1
server.listen()

client_socket, client_address = server.accept()

file = open('server.ppt', "wb")
image_chunk = client_socket.recv(100000)  # stream-based prool

while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(100000)
    print(image_chunk)

file.close()
client_socket.close()
