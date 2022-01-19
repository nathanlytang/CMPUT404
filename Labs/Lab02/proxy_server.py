import socket

HOST = ""
PORT = 8001
BUFFER_SIZE=1024

def main():
    host = "www.google.com"
    port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy:
        print("Starting proxy")
        proxy.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy.bind((HOST, PORT))
        proxy.listen(1)

        while True:
            conn, address = proxy.accept()
            print(f"Connected to {address}")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_conn:
                # Connect to remote address
                remote_ip = socket.gethostbyname(host)
                proxy_conn.connect((remote_ip, port))

                # Send data to remote address
                send_data = conn.recv(BUFFER_SIZE)
                proxy_conn.sendall(send_data)

                # Receive data back from remote address
                proxy_conn.shutdown(socket.SHUT_WR)
                data = proxy_conn.recv(BUFFER_SIZE)

                # Send data to client
                conn.send(data)

if __name__ == "__main__":
    main()
