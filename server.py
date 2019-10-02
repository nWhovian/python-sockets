import socket


def main():
    PORT = 8800
    number = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            string = conn.recv(1024).decode("utf-8")
            point_at = string.find('.')
            length = int(string[:point_at])
            string = string[point_at + 1:]
            string = string[:length]
            point_at = string.find('.')
            filename = string[:point_at] + '_' + str(number) + string[point_at:]
            with open(filename, "wb") as fw:
                while True:
                    data = conn.recv(1024)
                    if (not data) or (data == b'ENDED'):
                        break
                    elif data == b'BEGIN':
                        print('beginning to receive')
                        continue
                    else:
                        fw.write(data)
                fw.close()
                print('done with ' + filename)
            conn.close()
            number += 1


if __name__ == "__main__":
    main()
