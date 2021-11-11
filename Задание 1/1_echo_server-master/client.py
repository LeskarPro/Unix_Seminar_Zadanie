# import socket  # for sockets
# import sys  # for exit
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# host = 'localhost'
# port = 9000
#
# while 1:
#     msg = input('Enter message to send : ')
#     if msg == "exit":  # end the cycle
#         break
#     try:
#         # Set the whole string
#         s.sendto(bytes(msg, 'utf-8'), (host, port))
#
#         # receive data from client (data, addr)
#         d = s.recvfrom(1024)
#         reply = d[0]
#         addr = d[1]
#
#         print('Server reply : ', reply.decode())
#
#     except (socket.error, msg):
#         print(f'Error Code : ', str(msg[0]), ' Message ', msg[1])
#         sys.exit()

import socket
import sys

UDP_PORT = 9000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('localhost', UDP_PORT))

while 1:
    msg = input('Enter message to send : ')
    if msg == "exit":  # end the cycle
        break
    try:
        # Set the whole string
        s.send(bytes(msg, 'utf-8'))
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print('Server reply : ', reply.decode())

    except (socket.error, msg):
        print(f'Error Code : ', str(msg[0]), ' Message ', msg[1])
        sys.exit()