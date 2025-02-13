import socket
import threading


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW MEMBER] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False

                print(f"[{addr}] {msg}")
                conn.send("msg received".encode(FORMAT))

    conn.close()

def start():
    server.listen()
    print(f"[LISTEING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target= handle_client, args= (conn, addr))
        thread.start()
        print(f"[CONNECTED MEMBERS] {threading.activeCount() - 1}")



print("[starting] server is starting... ")
start()
