import socket
import random
from _thread import *

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 4444

threadNum = 0

word_to_num = {"rock": 0, "spock": 1, "paper": 2, "lizard": 3, "scissors": 4}
num_to_word = {0: "rock", 1: "spock", 2: "paper", 3: "lizard", 4: "scissors"}

try:
    serverSocket.bind((HOST, PORT))
except socket.error as e:
    print("error binding to port: ", PORT, " on host: ", HOST)
    print(str(e))

serverSocket.listen(3)
print("socket listening on port: ", PORT)


def play_game(human_choice):
    print("player has chosen: ", human_choice)

    player_number = word_to_num[human_choice]
    server_number = random.randrange(0, 4)

    server_choice = num_to_word[server_number]
    print("server has chosen: ", server_choice)

    diff = (server_number - player_number) % 5

    if diff == 0:
        result = "tie"
    elif diff < 3:
        result = "lose"
    else:
        result = "win"

    return result, server_choice


def client_handler(connection):
    while True:
        player_choice = connection.recv(1024)
        player_choice = player_choice.decode("utf-8")

        if not player_choice:
            print("message received is invalid, cannot decode!")
            connection.sendall(str.encode("error in receiving the message! Try again"))
        else:
            game_result, server_choice = play_game(player_choice)
            connection.sendall(str.encode(game_result))
            connection.sendall(str.encode(server_choice))

            if game_result in ("win", "lose"):
                break
    connection.close()


while True:
    if threadNum == 10:
        break

    (conn, addr) = serverSocket.accept()
    print("user with address: ", addr, " has connected")

    start_new_thread(client_handler, (conn,))
    threadNum += 1

    print("user with address: ", addr, " has disconnected")


serverSocket.close()
