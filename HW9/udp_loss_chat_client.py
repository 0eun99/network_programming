from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

c = socket(AF_INET, SOCK_DGRAM)
c.connect(('localhost', port))
print('connecnt')

while True:
    msg = input('-> ') 
    reqx = 0

    while reqx <= 3: #최대 3회 재전송
        reQx = str(reqx) + " " + msg #재전송 횟수 더해서 전송
        c.sendto(reQx.encode(),('localhost', port))
        c.settimeout(2) #타임아웃 2초
        
        try:
            data, addr = c.recvfrom(BUFF_SIZE)
        except timeout:
            reqx += 1 #타임아웃시 1 증가
            continue
        else:
            if data.decode() == "ack":
                break

    c.settimeout(None)
    while True: #50% 확률로 ack 보내지 X
        data, addr = c.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            c.sendto(b'ack', ('localhost', port))
            print('<-', data.decode())
            break

       
c.close()
