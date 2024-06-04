#SERVER SCRIPT 
import socket
import threading

# Global variables
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 55555
clients = {}
client_id_counter = 1
lock = threading.Lock()

def broadcast(message, client_socket=None):
    with lock:
        for client in clients:
            if client != client_socket:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    client.close()
                    remove_client(client)

def remove_client(client_socket):
    with lock:
        if client_socket in clients:
            del clients[client_socket]

def handle_client(client_socket):
    global client_id_counter
    with lock:
        client_id = client_id_counter
        client_id_counter += 1
        clients[client_socket] = client_id
    
    client_socket.send(f"[INFO] You are Client {client_id}".encode('utf-8'))
    broadcast(f"[INFO] Client {client_id} has joined the chat.", client_socket)
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(f"Client {client_id}: {message}", client_socket)
        except:
            break

    remove_client(client_socket)
    client_socket.close()
    broadcast(f"[INFO] Client {client_id} has left the chat.")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print("[STARTED] Server is running...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[CONNECTED] {client_address} connected.")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
