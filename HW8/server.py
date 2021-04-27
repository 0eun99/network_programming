import socket

port = 2000 
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))
    
mboxID={}

while True:
    recvMSG, addr = sock.recvfrom(BUFFSIZE)
    msg = recvMSG.decode()

    if msg == "quit":
        break
    msg = msg.split(' ') #공백 기준 끊어주기

    if msg[0] == 'send': #send가 도착하면
        plusmsg = msg[2:]
        finalmsg =' '.join(plusmsg) #문자열 합침(plusmsg)

        if msg[1] in mboxID:
            mboxID[msg[1]] += [finalmsg]
            print(mboxID)
            sock.sendto(b'ok', addr) #클라이언트로 ok 전송
            
        else:
            mboxID[msg[1]] = [finalmsg]
            print(mboxID)
            sock.sendto(b'ok', addr)

    elif msg[0] == "receive": #receive 도착하면
        if msg[1] in mboxID:
            word = mboxID.get([msg[1]][0])

            if word == []:
                sock.sendto(b'No Messages', addr)
            else:
                sendMSG = mboxID[msg[1]][0] #mboxID 제일 앞 메세지
                sock.sendto(sendMSG.encode(),addr) #전송
                del mboxID[msg[1]][0] #삭제
                print(mboxID)
        else:
            sock.sendto(b'No Messages', addr)


sock.close()    
