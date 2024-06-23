# Python Chat Application

A simple Python chat application with both command-line interface (CLI) and graphical user interface (GUI) clients. Built using sockets and Tkinter, the application supports text and file messaging with a multithreaded server for handling multiple clients.

## Features

- **Text Messaging**: Send and receive text messages in real-time.
- **File Transfer**: Send and receive files.
- **Multiclient Support**: Server can handle multiple clients simultaneously.
- **Graphical User Interface (GUI)**: User-friendly GUI client built with Tkinter.
- **Command-Line Interface (CLI)**: Lightweight CLI client for sending and receiving messages.

## Requirements

- Python 3.x
- Tkinter (for GUI client)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/python-chat-app.git
    cd python-chat-app
    ```

2. **Install dependencies**:
    - Tkinter is included with standard Python distributions. Ensure you have it installed.
    - If using a virtual environment, activate it:
      ```sh
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
      ```

## How to Run

### Server

1. **Start the server**:
    ```sh
    python server.py
    ```
    The server will start and listen on port `12345` for incoming connections.

### CLI Client

1. **Start the CLI client**:
    ```sh
    python cli_client.py
    ```
    You will be prompted to enter messages. Use the command `/sendfile <path>` to send a file.

### GUI Client

1. **Start the GUI client**:
    ```sh
    python gui_client.py
    ```
    A window will appear where you can enter messages and send files using buttons.

## Project Structure

python-chat-app/
│
├── cli_client.py # CLI client script
├── gui_client.py # GUI client script
├── server.py # Server script
├── README.md # Project readme file
├── LICENSE # Project license file
└── .gitignore # Git ignore file
## Usage

### CLI Client

- **Sending Text**: Type your message and press Enter.
- **Sending Files**: Use the command `/sendfile <path>` to send a file. For example:
    ```sh
    /sendfile /path/to/your/file.txt
    ```

### GUI Client

- **Sending Text**: Enter your message in the text entry field and click "Send".
- **Sending Files**: Click the "Send File" button and choose a file to send.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Acknowledgements

- [Python](https://www.python.org/) - The programming language used.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - The GUI library used.
- [Socket Programming](https://docs.python.org/3/library/socket.html) - Used for network communication.
