import re
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    #받아온 데이터에서 필요 없는 것들 생략(split 사용 문자열 자르기)
    re_data = re.split(" |/", req[0])
    data = re_data[2]
    print(data)

    #서버 코드 작성(파일 전송 후 닫기)
    if (data == 'index.html'):
        f = open('index.html', 'r', encoding='utf-8')
        mimeType = 'text/html'

        read_data = f.read() #파일 읽기

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n') #encode 잊지 말기
        c.send(b'\r\n')
        c.send(read_data.encode()) #html 파일 전송
    
    elif (data == 'favicon.ico'):
        f = open('favicon.ico', 'rb')
        mimeType = 'image/x-icon'

        read_data = f.read() #파일 읽기

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(read_data) #파일 전송
        
    elif (data == 'iot.png'):
        f = open('iot.png', 'rb')
        mimeType = 'image/png'

        read_data = f.read() #파일 읽기

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(read_data) #파일 전송

    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>NotFound</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
    
#각 객체 전송 후 소켓 닫기
c.close()