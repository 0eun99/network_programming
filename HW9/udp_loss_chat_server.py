from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None) #무한정 블로킹(timeout설정)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5: #50%의 확률로 응답 X
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break

    msg = input('->')
    reTx = 0
    
    while reTx <= 3: #재전송 횟수가 3번 이하인 경우 메시지 전송
        resp = str(reTx) + ' '+ msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2) #타임아웃 2초

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout: #타임아웃 발생시 
                reTx += 1 #재전송 횟수 1 증가
                continue
        else:
            break
sock.close()

