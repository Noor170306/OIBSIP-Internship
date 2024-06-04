#CLIENT SCRIPT 
import socket
import threading

# Global variables
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 55555

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except Exception as e:
            print(f"[ERROR] {e}")
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("[CONNECTED] Connected to the server.")
        
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        while True:
            message = input("")
            if message:
                
                client_socket.send(message.encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] : {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
