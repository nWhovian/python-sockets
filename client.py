#!/usr/bin/env python3

import socket
import sys
import os


def main():
    file = sys.argv[1]
    HOST = sys.argv[2]
    PORT = int(sys.argv[3])

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        size = os.path.getsize(file)
        iteration = 1
        with open(file, 'rb') as fs:
            s.send(bytes(str(len(file)) + '.' + file, 'utf-8'))
            s.send(b'BEGIN')
            while True:
                data = fs.read(1024)
                print('Sending data: ~' + str(min(100, round((iteration * 1024 * 100) / size, 2))) + '% done')
                s.send(data)
                iteration += 1
                if not data:
                    print('Done!')
                    break
            s.send(b'ENDED')
            fs.close()
        s.close()


if __name__ == "__main__":
    main()
