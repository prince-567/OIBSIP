#Prince
        # Task NO-3 Chat Application (Server Side)

import socket
import threading
# Store connected clients
clients = []

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg, client)
        except:
            clients.remove(client)
            client.close()
            break

def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()

    # print("Server started on port 12345...")

    while True:
        client, addr = server.accept()
        print(f"Connected with {addr}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    main()
