#Prince
        # Task No-3 Chat Application (Client Server)
import socket
import threading

def receive(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            print("Disconnected from server.")
            break

def send(client):
    while True:
        msg = input()
        client.send(msg.encode())

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    print("Connected to the server.")
    name = input("Enter your name: ")
    client.send(f"{name} joined the chat.".encode())

    # Threads for send and receive
    threading.Thread(target=receive, args=(client,), daemon=True).start()
    threading.Thread(target=send, args=(client,), daemon=True).start()

    while True:
        pass

if __name__ == "__main__":
    main()
