import socket
import os
import sys
import threading

IP = '127.0.0.1'  # default IP address of the server
PORT = 12000  # change to a desired port number
BUFFER_SIZE = 1024  # change to a desired buffer size


def get_file_info(data: bytes) -> (str, int):
    return data[8:].decode(), int.from_bytes(data[:8], byteorder='big')


def upload_file(conn_socket: socket, file_name: str, file_size: int):
    # create a new file to store the received data
    file_name += '.temp'
    # please do not change the above line!
    with open(file_name, 'wb') as file:
        retrieved_size = 0
        try:
            while retrieved_size < file_size:
                # TODO: section 3 step 6a
                chunk = conn_socket.recv(BUFFER_SIZE)
                # TODO: section 3 stop 6b
                retrieved_size = len(chunk)
                # TODO: section 3 stop 6c
                file.write(chunk)
                file_size -= retrieved_size
        except OSError as oe:
            print(oe)
            os.remove(file_name)


def service_client_connection(conn_socket: socket):
    try:
        # TODO: section 3 step 2
        message = conn_socket.recv(BUFFER_SIZE)
        # expecting an 8-byte byte string for file size followed by file name

        # TODO: section 3 step 3
        file_name, file_size = get_file_info(message)

        print(f'Received: {file_name} with size = {file_size}')
        # TODO: section 3 step 4
        conn_socket.sendto(b'go ahead', (IP, PORT))
        upload_file(conn_socket, file_name, file_size)
    except Exception as e:
        print(e)
    finally:
        conn_socket.close()


def start_server(ip, port):
    # create a TCP socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))  # section 3 and 4 step 1
    server_socket.listen(5)  # section 4 step 2
    print(f'Server ready and listening on {ip}:{port}')
    try:
        while True:  # section 4 step 6
            (conn_socket, addr) = server_socket.accept()  # section 4 step 3
            # TODO: section 4 step 4
            thread = threading.Thread(target=service_client_connection, args=(conn_socket,))
            # TODO: section 4 step 5
            thread.start()
    except KeyboardInterrupt as ki:
        pass
    finally:
        server_socket.close()


if __name__ == '__main__':
    # get IP address from cmd line
    if len(sys.argv) == 2:
        IP = sys.argv[1]  # IP from cmdline argument

    start_server(IP, PORT)
