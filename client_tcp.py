import socket
import sys


def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:
        print('Connection is fail')
        print(f'Error: {e}')
        sys.exit()

    target = input('Write a target (host:port): ')
    target = target.split(':')
    host = target[0]
    port = int(target[1])

    try:
        connection.connect((host, port))
        print(f'Success in connect TCP {host}:{port}')
        connection.shutdown(2)

    except socket.error as e:
        print(f'Connection is fail in target: {host}:{port}')
        print(f'Error: {e}')
        sys.exit()


if __name__ == '__main__':
    main()
