days = { 'January':31, 'February':28, 'March':31, 'April':30, 
        'May':31, 'June':30, 'July':31, 'August':31,
        'September':30, 'October':31, 'November':30, 
        'December':31 }
        

#1.월 입력 시 해당 일수를 출력하기
user_input = input("write here: ")

for key in days:
    if key == user_input:
        print(days[key])


#2.알파벳 순서로 모든 월을 출력하기
print( sorted(days.keys()), end='\n\n')


#3.일수가 31일인 월을 모두 출력하기
for key in days:
    if days[key] == 31:
        print(key, end=' | ')
print('\n\n')


#4.월의 일수를 기준으로 오름차순인(key-value)쌍 출력하기
Sortdays = sorted(days.items(), key=lambda t: t[1])
print(Sortdays)


#5.사용자가 월을 3자리만 입력시, 월의 일수를 출력하기
user_input2 = input('write here: ')

if len(user_input2) == 3:
    for key in days:
        if user_input2 in key :
            print(days[key])
else:
    print('write 3 letters!')
