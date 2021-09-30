import socket
import sys

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 9000  # Arbitrary non-privileged port
msg = ''
# Datagram (udp) socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket created')

s.bind((HOST, PORT))

print('Socket bind complete')

# now keep talking with the client
while 1:

    # receive data from client (data, addr)

    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    if not data:
        break

    print('Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + str(data.strip()))
    reply = data.decode()
    s.sendto(bytes(reply, 'utf-8'), addr)

s.close()
