import socket

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHOST: www.google.com\r\n\r\n"

def connect(address):
    try:
        # Connect to the proxy server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)

        # Send payload to proxy
        sock.sendall(payload.encode())
        sock.shutdown(socket.SHUT_WR)

        # Get data
        data = sock.recv(BUFFER_SIZE)
        print(data)

        # Close connection
        sock.close()

    except Exception as exception:
        print(exception)

def main():
    connect((HOST, PORT))

if __name__ == "__main__":
    main()