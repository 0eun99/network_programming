from socket import *
from random import *
import sys

BUF_SIZE = 1024
#LENGTH = 20

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 77))

#s.send(b'Hello') # ‘Hello’ 메시지 전송
while True:
    rec = s.recv(BUF_SIZE) #메시지 수신
    msg = rec.decode()

    if not msg :
        break
    elif msg == "2":
        heart = randint(40, 140) #0~40 사이의 온도값
        step = randint(2000, 6000) #0~100 사이의 습도값
        cal = randint(1000, 4000) #70~150 사이의 조도값

        #data = "Heartbeat=", heart, "Steps=", step, "Cal=", cal
        #print("보내는 데이터 값: ", data)
        final = "Device2: Heartbeat={}, Steps={}, Cal={}".format(heart, step, cal)
        print("보내는 데이터 값: ", final.decode())
        s.send(final.encode()) #값 전송

s.close()