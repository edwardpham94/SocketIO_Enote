import socket
import threading
import pickle

PORT = 80
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.100.2"
ADDR = (SERVER, PORT)

# Send a message as string to the server
def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

# Send a list of elements by using pickle
def sendList(client, lst):
    data = pickle.dumps(lst)
    client.send(data)

# Thread to recive message from the other client
def reciveMessage(client):
    while True:
        print(client.recv(2048).decode(FORMAT))

def inputUser(client):
    while True:
        username = input("user: ")
        password = input("pass: ")
        sendList(client, [username, password])
        print(client.recv(2048).decode(FORMAT))

if __name__ == "__main__":
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
        
        thread1 = threading.Thread(target=reciveMessage, args=(client,))
        thread1.start()

        thread2 = threading.Thread(target=inputUser, args=(client,))
        thread2.start()
  
    except:
        print("Error")
        input()