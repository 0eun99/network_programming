from socket import *

BUFFSIZE = 1024
port = 2000

c = socket(AF_INET, SOCK_DGRAM)
c.connect(('localhost', port))

while True:
    request = input('send or receive +num +string: ')
    if request == "quit":
        c.sendto(request.encode())
        break

    c.send(request.encode())
    recvData, addr = c.recvfrom(BUFFSIZE)
    data = recvData.decode()
    print(data)

c.close()