from random import randint

start_coin = 50 #시작 코인
large_coin = 100 #최대 코인
small_coin = 0 #최소 코인
guess = 0 #예상 숫자

while start_coin <= large_coin and start_coin >= small_coin : 
    coin = randint(1,2) #1 또는 2를 임의로 발생
    guess = eval(input('Enter your guess(1,2): '))
    if guess == coin: #숫자를 맞추면 9코인 얻고 틀리면 10코인 잃음
        start_coin = start_coin + 9
        print('맞았습니다!', start_coin)
    
    elif guess != coin:
        start_coin = start_coin - 10
        print('틀렸습니다!', start_coin)

if start_coin <= 0 :
    print('코인을 전부 잃었습니다.')

elif start_coin >= 100 :
    print('축하합니다. 최대 코인을 획득했습니다.')
