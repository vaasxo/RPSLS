import socket
from _thread import *

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = '4444'

try:
    serverSocket.bind((HOST, PORT))
except socket.error as e:
    print("error binding to port: ", PORT, " on host: ", HOST)
    print(str(e))

serverSocket.listen(3)
print("socket listening on port: ", PORT)


def client_handler(connection):
    while True:
        player_choice = connection.recv(1024)
        player_choice.decode('UTF-8')

        if not player_choice:
            print("message received is invalid, cannot decode!")
            connection.sendall(str.encode("error in receiving the message! Try again"))
            break
        else:
            print("message received: ", player_choice)
    connection.close()
    return 0


while True:
    (conn, addr) = serverSocket.accept()
    print("user with address: ", addr, " has connected")
    start_new_thread(client_handler, (conn,))
    conn.close()
    print("user with address: ", addr, " has disconnected")

serverSocket.close()
