from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 5555))

while True:
    msg = input('계산식을 입력하세요: ')
    if msg == 'q':
        break
    
    s.send(msg.encode()) #계산식 서버로 전송

    print('결과:', s.recv(1024).decode()) #결과 출력

s.close()