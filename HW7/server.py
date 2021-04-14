from socket import *
import os
import time
import sys

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 77))
sock.listen(10)
print('Server is running...')

conn1, addr1 = sock.accept()
conn2, addr2 = sock.accept()
print('client:', addr1)
print('client:', addr2)

while True:
    request = input('연결하려는 디바이스를 입력하세요(1,2): ')

    if request == b"quit":
        conn1.send(request.encode())
        conn2.send(request.encode())
        break

    elif request == b"1":
        conn1.send(request.encode()) #디바이스 번호 전송
        msg1 = conn1.recv(BUF_SIZE) #데이터 수신
        msg_1 = msg1.decode()
        print('받은 데이터 값 :', msg1.decode()) #받은 요청 출력
        if not msg1:
            break

        f = open("C:/Users/csi0647/network_programming/HW7/data.txt", 'a')
        t = time.strftime('%c', time.localtime(time.time()))
        f.write("{0}:{1}\r\n".format(t, msg_1))
        f.close()
        
    elif request == b"2":
        conn2.send(request.encode()) #디바이스 번호 전송
        msg2 = conn2.recv(BUF_SIZE) #데이터 수신
        msg_2 = msg2.decode()
        print('받은 데이터 값 :', msg2.decode()) #받은 요청 출력
        if not msg2:
            break

        f = open("C:/Users/csi0647/network_programming/HW7/data.txt", 'a')
        t = time.strftime('%c', time.localtime(time.time()))
        f.write("{0}:{1}\r\n".format(t, msg_2))
        f.close()
    continue

sock.close()
