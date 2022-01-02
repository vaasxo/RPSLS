import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = '4444'

try:
    clientSocket.connect((HOST, PORT))
except socket.error as e:
    print("error connecting to server! Please try again")
    print(str(e))

while True:
    player_choice = "abc"
    clientSocket.send(str.encode(player_choice))

    result = clientSocket.recv(1024)
    print(result.decode('UTF-8'))

clientSocket.close()

