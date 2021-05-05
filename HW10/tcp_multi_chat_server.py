from socket import *
import threading
import time

port = 3333
BUFFSIZE = 1024

clients = [] #클라이언트 목록

#accept해서 conn(소켓 자체)에 넣었으니 
#주소가 아니라 소켓을 불러와야(addr X, conn O)
#기존에 할당받은 소켓들을 비교해서 값을 보낼 수 있음

def recvTask(conn):
    while True:
        data = conn.recv(BUFFSIZE)
        if not data:
            break

        elif 'quit' in data.decode():
            if conn in clients:
                print(conn, 'exited')
                clients.remove(conn)

        #모든 클라이언트에게 전송
        for client in clients:
            if client != conn:
                client.send(data)
        print(time.asctime() + str(addr) + ':' + data.decode())


s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(4)

while True :
    conn, addr = s.accept() 

    th = threading.Thread(target=recvTask, args=(conn,))
    th.start()

    #새로운 클라이언트 목록에 추가    
    if addr not in clients:
        print('new client', addr)
        clients.append(conn)
