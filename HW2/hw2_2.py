A = eval(input('Enter number(A): '))
B = eval(input('Enter number(B): '))

def gcd(x,y):
    if x>y:
        target = x
        subtarget = y
    else:
        target = y
        subtarget = x

    Remaining = target % subtarget
    if Remaining != 0:
        return gcd(subtarget,Remaining)

    else:
        return subtarget

print('최대 공약수 : ', gcd(A,B))