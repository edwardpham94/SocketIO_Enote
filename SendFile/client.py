import socket

# AF_INET = IP, SOCK_STREAM = TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1002))  # 127.0.0.1

file = open('21.ppt', 'rb')
image_data = file.read(100000)

while image_data:
    client.send(image_data)
    image_data = file.read(100000)

file.close()
client.close()
