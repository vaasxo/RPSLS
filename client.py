import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 4444

possible_choices = ("rock", "paper", "scissors", "lizard", "spock")

try:
    clientSocket.connect((HOST, PORT))
except socket.error as e:
    print("error connecting to server! Please try again")
    print(str(e))


def get_input():
    player_input = input("Please enter your choice: ")
    if player_input.lower() not in possible_choices:
        player_input = input("Oops! You entered an invalid option, please choose from the following: rock, paper, "
                             "scissors, lizard, spock")
    return player_input.lower()


while True:
    print("Welcome to rock-paper-scissors-lizard-spock! \n")

    player_choice = get_input()
    clientSocket.send(str.encode(player_choice))

    result = clientSocket.recv(1024)
    result = result.decode("utf-8")

    if result not in ("win", "lose", "tie"):
        print(result)
        continue

    server_choice = clientSocket.recv(1024)
    server_choice = server_choice.decode("utf-8")

    if result == "win":
        print("The server chose: ", server_choice, "\n\n You win!")
        break
    elif result == "tie":
        print("The server chose: ", server_choice, ". It's a tie, so, try again!")
    else:
        print("The server chose: ", server_choice, "\n\n You lose!")
        break

clientSocket.close()
