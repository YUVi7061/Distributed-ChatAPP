# gui_client.py

import tkinter as tk
import threading
import socket
import json
import base64
import tkinter.filedialog

def receive_messages():
    while True:
        try:
            message = client_socket.recv(4096).decode()
            msg_data = json.loads(message)

            if msg_data["type"] == "file":
                file_data = base64.b64decode(msg_data["data"])
                save_path = f"received_{msg_data['filename']}"
                with open(save_path, "wb") as file:
                    file.write(file_data)
                chat_text.insert(tk.END, f"Received file and saved as {save_path}\n", "received")
            else:
                chat_text.insert(tk.END, f"Received: {msg_data['message']}\n", "received")

        except (OSError, ConnectionError) as e:
            print(f"Error receiving message: {e}")
            break

def send_message():
    message = message_entry.get()
    if message:
        msg_data = {
            "type": "text",
            "message": message
        }
        chat_text.insert(tk.END, f"Sent: {message}\n", "sent")
        client_socket.send(json.dumps(msg_data).encode())
        message_entry.delete(0, tk.END)

def send_file():
    file_path = tk.filedialog.askopenfilename()
    if not file_path:
        return

    with open(file_path, "rb") as file:
        encoded_file_data = base64.b64encode(file.read()).decode()

    filename = file_path.split("/")[-1]
    file_msg = {
        "type": "file",
        "filename": filename,
        "data": encoded_file_data
    }
    client_socket.send(json.dumps(file_msg).encode())
    chat_text.insert(tk.END, f"Sent file: {filename}\n", "sent")

def connect_to_server():
    global client_socket
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    connect_button.config(state=tk.DISABLED)

    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

def disconnect_from_server():
    if client_socket:
        client_socket.close()
        connect_button.config(state=tk.NORMAL)

client_socket = None

client_gui = tk.Tk()
client_gui.title("Chat Application")

chat_text = tk.Text(client_gui)
chat_text.pack()

message_entry = tk.Entry(client_gui)
message_entry.pack()

send_button = tk.Button(client_gui, text="Send", command=send_message)
send_button.pack()

send_file_button = tk.Button(client_gui, text="Send File", command=send_file)
send_file_button.pack()

connect_button = tk.Button(client_gui, text="Connect to Server", command=connect_to_server)
connect_button.pack()

disconnect_button = tk.Button(client_gui, text="Disconnect", command=disconnect_from_server)
disconnect_button.pack()

chat_text.tag_config("sent", foreground="blue")
chat_text.tag_config("received", foreground="green")

client_gui.mainloop()
    
