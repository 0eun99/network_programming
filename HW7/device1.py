from socket import *
from random import *
import sys

BUF_SIZE = 1024
#LENGTH = 20
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 77))

while True:
    rec = s.recv(BUF_SIZE) #메시지 수신
    msg = rec.decode()

    if not msg :
        break
    elif msg == b"1":
        temp = randint(0, 40) #0~40 사이의 온도값
        hum = randint(0, 100) #0~100 사이의 습도값
        lu = randint(70, 150) #70~150 사이의 조도값

        #data = "Temp=", temp, "Humid=", hum, "lilum=", lu
        #print("보내는 데이터 값: ", data)
        final = "Device1: Temp={}, Humid={}, linum={}".format(temp, hum, lu)
        print("보내는 데이터 값: ", final.decode())

        s.send(final.encode()) #온습조도값 전송
    elif msg == "quit":
        break
s.close()