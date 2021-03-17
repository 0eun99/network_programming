i = 1
num=[]
sum = 0
while True:
    if i <=1000:
        num.append(str(i))
        i+=1
    else:
        break

for i in num:
    sum += int(i)

print(sum)