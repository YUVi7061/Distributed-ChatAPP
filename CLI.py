# cli_client.py

import socket
import threading
import json
import base64

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(4096).decode()
            msg_data = json.loads(message)

            if msg_data["type"] == "file":
                file_data = base64.b64decode(msg_data["data"])
                save_path = f"received_{msg_data['filename']}"
                with open(save_path, "wb") as file:
                    file.write(file_data)
                print(f"Received file and saved as {save_path}")
            else:
                print(msg_data["message"])

        except:
            print("Connection lost.")
            break

def send_message(client_socket):
    while True:
        message_input = input()

        if message_input.startswith("/sendfile "):
            file_path = message_input.split(' ', 1)[1]
            try:
                with open(file_path, "rb") as file:
                    encoded_file_data = base64.b64encode(file.read()).decode()

                filename = file_path.split("/")[-1]
                msg_data = {
                    "type": "file",
                    "filename": filename,
                    "data": encoded_file_data
                }
            except FileNotFoundError:
                print("File not found!")
                continue
        else:
            msg_data = {
                "type": "text",
                "message": message_input
            }

        client_socket.send(json.dumps(msg_data).encode())

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    client.connect((server_ip, 12345))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_message, args=(client,))
    send_thread.start()

if __name__ == "__main__":
    main()
