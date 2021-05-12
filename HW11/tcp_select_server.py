#서버
# from socket import *
import time
import socket, select

port = 3333
BUFFSIZE = 1024
socks = [] #소켓 리스트 

s_sock = socket.socket() #TCP 소켓
s_sock.bind(('', port))
s_sock.listen(4)

socks.append(s_sock) #서버 소켓 추가
print(str(port) + '에서 접속 대기 중')

while True :
    #읽기 이벤트(연결 요청 및 데이터 수신) 대기
    r_sock, w_sock, e_sock = select.select(socks, socks, [])

    for s in r_sock: #수신(읽기 가능한) 소켓 리스트 검사
        if s == s_sock: #연결 요청이 발생하면
            c_sock, addr = s_sock.accept() #클라이언트 연결
            if c_sock not in socks:
                socks.append(c_sock) #연결된 애 소켓 리스트에 저장
                print('client ({}) connectes'.format(addr))
        else:
            data = s.recv(BUFFSIZE)
            if not data:
                break
            elif 'quit' in data.decode():
                if s in socks: #연결된 소켓이 저장된 곳에 있다면
                    print(addr, 'exited')
                    s.close()
                    socks.remove(s) #종료된 애 리스트에서 제거
                    continue
            for client in w_sock: #모든 클라이언트에게 전송 //w_sock말고 socks로 하면 client.send 사용 불가 + 쓰기 가능 여부를 검사할걸 설정을 안해놨었음. 빈 리스트로 해두니 안되던 것!
                if client != s: #지금 채팅 보내는 애를 제외한 다른 애들한테만 값 보내도록 설정
                    client.send(data)
            print(time.asctime() + str(addr) + ':' + data.decode())



