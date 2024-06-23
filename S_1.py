# server.py

import socket
import threading
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)

clients = []

def broadcast(message, from_socket):
    for client in clients:
        if client != from_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)
                client.close()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(4096)
            if not message:
                break

            broadcast(message, client_socket)

        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def main():
    print("Server is running...")
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f'Client {addr[0]} connected.')
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
