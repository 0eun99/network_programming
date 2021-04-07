from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 5555))
s.listen(5)
print('waiting...')

#operator = ["+", "-", "/", "*"]
#string_list = []

while True:
    Client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = Client.recv(1024) #클라이언트로 부터 데이터 수신
        print('받은 계산식 :', data.decode())#받은 데이터 출력
        if not data:
            break
        
        try: 
            rsp = format(eval(data),".1f")#계산 함수 eval + 소수점 1자리까지
        except:
            Client.send(b'Try again')
        else:
            Client.send(rsp.encode())#데이터 전송

    Client.close()